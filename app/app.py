import os
import sys
import time
import gevent

from shutil import copyfile, move
from json import dumps
from flask import Flask, abort, render_template, jsonify, request, make_response
from flask_socketio import SocketIO, emit

from sense import SensorThread
from control import ControlThread
from rules import Rule, RuleEngine

app = Flask(__name__)
app.config['SECRET_KEY'] = 'webrover1'
socketio = SocketIO(app)
sense = SensorThread(socketio)
control = ControlThread()
rule_engine = RuleEngine(control)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('four_oh_four.html'), 404

@app.route('/')
def index():
    control.reset()
    return render_template('index.html', title='WebRover1')

@socketio.on('action')
def action(*args):
    control.operation('action', args)

@socketio.on('camera')
def camera(*args):
    control.operation('camera', args)

@socketio.on('delay')
def handle_delay(delay):
    print('new delay: ' + delay)
    control.set_delay(int(delay))

@socketio.on('rule')
def handle_rule(rule):
    print('new rule: ' + rule)

current_rules = []
@app.route('/api/rules/', methods=['GET', 'POST'])
def rules():
    global current_rules
    if request.method == 'POST':
        print request.json
        current_rules = request.json
        compiled_rules = []
        for rule in request.json:
            title = rule['title']
            trigger = rule['trigger']
            actions = rule['actions']
            print "rule: %s" % title
            compiled_rules.append(Rule(trigger['title'], (a['title'] for a in actions)))
        rule_engine.activate(compiled_rules)
        return jsonify(result='ok')

    # else
    return make_response(dumps(current_rules))


@app.route('/camera/')
def camera():
    return render_template('camera.html')

# just pass these on for rtc
@socketio.on('offer')
def offer(data):
    print 'offer'
    emit('offer', data, broadcast=True)
@socketio.on('answer')
def answer(data):
    print 'answer'
    emit('answer', data, broadcast=True)
@socketio.on('offer ice')
def offer_ice(data):
    print 'offer ice'
    emit('offer ice', data, broadcast=True)
@socketio.on('answer ice')
def answer_ice(data):
    print 'answer ice'
    emit('answer ice', data, broadcast=True)


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'nxt2':
        import nxt2
        robot = nxt2
    else:
        import ev3
        robot = ev3
    control.start(sense, rule_engine, robot)
    print 'running socketio'
    socketio.run(app, host='0.0.0.0', port=5000) #, debug=True)
