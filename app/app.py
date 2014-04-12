from flask import Flask, abort, render_template
import sys
import nxt.locator
from nxt.motor import *
from time import sleep
from nxt.sensor import *


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
        b = nxt.locator.find_one_brick()
        m_left = Motor(b, PORT_B)
        m_right = Motor(b, PORT_C)
        m_left.run(power=100)
        m_right.run(power=100)
        sleep(0.3)
        m_left.idle()
        m_right.idle()
        return 'success'
    except:
        abort(404)


@app.route('/stop/')
def stop():
    '''
    Stop the robot
    '''
    try:
        b = nxt.locator.find_one_brick()
        m_left = Motor(b, PORT_B)
        m_right = Motor(b, PORT_C)
        m_left.idle()
        m_right.idle()
        return 'success'
    except:
        abort(404)


@app.route('/right/')
def right():
    try:
        b = nxt.locator.find_one_brick()
        m_left = Motor(b, PORT_B)
        m_right = Motor(b, PORT_C)
        m_right.idle()
        m_left.idle()
        m_right.run(power=-100)
        m_left.run(power=100)
        sleep(0.3)
        m_right.idle()
        m_left.idle()
        return 'success'
    except:
        abort(404)


@app.route('/left/')
def left():
    try:
        b = nxt.locator.find_one_brick()
        m_left = Motor(b, PORT_B)
        m_right = Motor(b, PORT_C)
        m_left.run(power=-100)
        m_right.run(power=-100)
        sleep(0.5)
        m_right.idle()
        m_left.idle()
        m_right.run(power=100)
        m_left.run(power=-100)
        sleep(0.7)
        m_right.idle()
        m_left.idle()
        return 'success'
    except:
        abort(404)


@app.route('/spin/')
def spin():
    return 'success'

if __name__ == '__main__':
    app.run(debug=True)
