import sys
from time import sleep
from shutil import copyfile
from flask import Flask, abort, render_template, jsonify, request
from flask_socketio import SocketIO

from sense import SensorThread
from control import ControlThread


app = Flask(__name__)
app.config['SECRET_KEY'] = 'webrover1'
socketio = SocketIO(app)
sense = SensorThread(socketio)
control = ControlThread()


@app.errorhandler(404)
def page_not_found(error):
    return render_template('four_oh_four.html'), 404

@app.route('/')
def index():
    return render_template('index.html', title='WebRover1')

@socketio.on('action')
def action(*args):
    control.queue.put(args)

@socketio.on('camera')
def camera(direction):
    if direction == 'left':
        robot.camera_left()
    elif direction == 'right':
        robot.camera_right()

@socketio.on('delay')
def handle_delay(delay):
    print('new delay: ' + delay)
    control.delay = int(delay)

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
    return control.delay

def camera_offline():
    copyfile('/home/robot/webrover1/app/static/images/camera-offline.jpg', '/home/robot/webrover1/app/static/images/camera.jpg')


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'nxt2':
        import nxt2
        robot = nxt2
    else:
        import ev3
        robot = ev3
    camera_offline()
    sense.start(robot)
    control.start(robot)
    print 'running socketio'
    socketio.run(app, host='0.0.0.0', port=5000) #, debug=True)
