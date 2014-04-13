from time import sleep
import nxt.locator
from nxt.motor import *
from nxt.sensor import *

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
    m_left.idle()
    m_right.idle()

def stop():
    '''
    Stop the robot
    '''
    b = nxt.locator.find_one_brick()
    m_left = Motor(b, PORT_B)
    m_right = Motor(b, PORT_C)
    m_left.idle()
    m_right.idle()


def spin_right():
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

def spin_left():
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
