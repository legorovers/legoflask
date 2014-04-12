from flask import Flask, render_template
import sys
import nxt.locator
from nxt.motor import *
from time import sleep
from nxt.sensor import *


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', title='PiStorms Mars Rover')


@app.route('/forward/')
def forward():
    '''
    Move the robot forward
    '''
    b = nxt.locator.find_one_brick()
    m_left = Motor(b, PORT_B)
    m_right = Motor(b, PORT_C)
    m_left.run(power=100)
    m_right.run(power=100)
    sleep(0.3)
    return 'success'


@app.route('/stop/')
def stop():
    '''
    Stop the robot
    '''
    b = nxt.locator.find_one_brick()
    m_left = Motor(b, PORT_B)
    m_right = Motor(b, PORT_C)
    m_left.idle()
    m_right.idle()
    return 'success'


@app.route('/right/')
def right():
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


@app.route('/left/')
def left():
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


@app.route('/spin/')
def spin():
    return 'success'

if __name__ == '__main__':
    app.run(debug=True)
