import sys
from time import sleep
from flask import Flask, abort, render_template, jsonify, request
from flask_socketio import SocketIO

from sense import SensorThread


app = Flask(__name__)
app.config['SECRET_KEY'] = 'webrover1'
socketio = SocketIO(app)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('four_oh_four.html'), 404

@app.route('/')
def index():
    return render_template('index.html', title='WebRover1')

@socketio.on('action')
def action(direction, speed):
    if direction == 'forward':
        robot.forward()
    elif direction == 'left':
        robot.spin_left()
    elif direction == 'right':
        robot.spin_right()
    elif direction == 'reverse':
        robot.backward()
    else:
        robot.stop()

@socketio.on('delay')
def handle_delay(delay):
    print('new delay: ' + delay)

@socketio.on('rule')
def handle_rule(rule):
    print('new rule: ' + rule)

@app.route('/api/rules/', methods=['GET', 'POST'])
def rules():
    if request.method == 'POST':
        print request.json
        for rule in request.json:
            title = rule['title']
            trigger = rule['trigger']
            actions = rule['actions']
            print "rule: %s" % title
    return jsonify(result='ok')


@app.route('/camera/')
def camera():
    return render_template('camera.html')

@app.route('/upload/', methods=['POST'])
def upload():
    file = open('/home/robot/webrover1/app/static/images/camera.jpg', 'wb')
    file.write(request.get_data())
    file.close()
    socketio.emit('refresh')
    return 'success'


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'nxt2':
        import nxt2
        robot = nxt2
    else:
        import ev3
        robot = ev3
    thread = SensorThread(robot, socketio)
    print 'running socketio'
    socketio.run(app, host='0.0.0.0', port=5000) #, debug=True)
