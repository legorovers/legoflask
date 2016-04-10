import sys
from time import sleep
from shutil import copyfile, move
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
    control.operation('action', args)

@socketio.on('camera')
def camera(*args):
    control.operation('camera', args)

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

IMG_DIR = '/home/robot/webrover1/app/static/images/'
@app.route('/upload/', methods=['POST'])
def upload():
    file = open(IMG_DIR + 'camera-upload.jpg', 'wb')
    file.write(request.get_data())
    file.close()
    move(IMG_DIR + 'camera-upload.jpg', IMG_DIR + 'camera.jpg')
    # delay is handled in the camera browser
    socketio.emit('refresh')
    return str(control.delay)

def camera_offline():
    copyfile(IMG_DIR + 'camera-offline.jpg', IMG_DIR + 'camera.jpg')


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
