from flask import Flask, abort, render_template
import sys
import nxt2
import ev
from time import sleep

app = Flask(__name__)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('four_oh_four.html'), 404


@app.route('/')
def index():
    return render_template('index.html', title='PiStorms Mars Rover')


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


@app.route('/right/')
def right():
    try:
        robot.right()
        return 'success'
    except:
        abort(404)


@app.route('/left/')
def left():
    try:
        robot.left()
        return 'success'
    except:
        abort(404)


@app.route('/spin/')
def spin():
    return 'success'

if __name__ == '__main__':
    if sys.argv[1] == 'ev3':
        robot = ev
    else:
        robot = nxt2
    app.run(debug=True, host='0.0.0.0', port=80)
