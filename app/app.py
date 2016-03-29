from flask import Flask, abort, render_template, jsonify, request
from flask_socketio import SocketIO
import sys
from time import sleep

from sense import SensorThread

app = Flask(__name__)
app.config['SECRET_KEY'] = 'webrover1'
socketio = SocketIO(app)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('four_oh_four.html'), 404

@app.route('/')
def index():
    return render_template('index.html', title='PiStorms Mars Rover')

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

@app.route('/forward/')
def forward():
    '''
    Move the robot forward
    '''
    try:
        robot.forward()
        return 'success'
    except:
        abort(404)


@app.route('/stop/')
def stop():
    '''
    Stop the robot
    '''
    try:
        robot.stop()
        return 'success'
    except:
        abort(404)

@app.route('/reverse/')
def backward():
    try:
        robot.backward()
        return 'success'
    except:
        abort(404)


@app.route('/right/')
def right():
    try:
        robot.spin_right()
        return 'success'
    except Exception as e:
        print e
        abort(404)


@app.route('/left/')
def left():
    try:
        robot.spin_left()
        return 'success'
    except:
        abort(404)

@app.route('/api/delay/<int:delay_in>')
def set_delay(delay_in):
    try:
        robot.set_delay(delay_in/1000.0)
        return 'success'
    except:
        abort(404)

@app.route('/spin/')
def spin():
    return 'success'

@app.route('/api/sense/')
def distance():
    try:
        return jsonify(distance=robot.distance())
    except Exception as e:
        print e
        abort(404)

@socketio.on('delay')
def handle_delay(delay):
    print('new delay: ' + delay)

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

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'nxt2':
        import nxt2
        robot = nxt2
    else:
        import ev3
        robot = ev3
    thread = SensorThread(robot, socketio)
    socketio.run(app, host='0.0.0.0', port=5443, keyfile='legorover.key', certfile='legorover.crt', debug=True)
