from time import sleep
from ev3.ev3dev import *

A = 0x01
B = 0x02
C = 0x04
D = 0x08

right = B
left = C
both = B+C

delay=0

def set_delay(delay_in):
    global delay
    delay=delay_in
    print "setting delay to %s" % delay

def forward():
    '''
    Move the robot forward
    '''
    sleep(delay)
    a=Motor(port=Motor.PORT.A)
    a.reset()
    a.run_position_limited(700, 255, stop_mode=Motor.STOP_MODE.HOLD)
    b=Motor(port=Motor.PORT.B)
    b.reset()
    b.run_position_limited(700, 255, stop_mode=Motor.STOP_MODE.HOLD)

def backward():
    '''
    Reverse
    '''
    sleep(delay)
    a=Motor(port=Motor.PORT.A)
    a.reset()
    a.run_position_limited(-360, 255, stop_mode=Motor.STOP_MODE.HOLD)
    b=Motor(port=Motor.PORT.B)
    b.reset()
    b.run_position_limited(-360, 255, stop_mode=Motor.STOP_MODE.HOLD)

def stop():
    '''
    Stop the robot
    '''
    sleep(delay)
    motordevice.stop(both, brake=1)

def spin_right():
    sleep(delay)
    a=Motor(port=Motor.PORT.A)
    a.reset()
    a.run_position_limited(60, 255, stop_mode=Motor.STOP_MODE.HOLD)
    b=Motor(port=Motor.PORT.B)
    b.reset()
    b.run_position_limited(-60, 255, stop_mode=Motor.STOP_MODE.HOLD)

def spin_left():
    sleep(delay)
    a=Motor(port=Motor.PORT.A)
    a.reset()
    a.run_position_limited(-60, 255, stop_mode=Motor.STOP_MODE.HOLD)
    b=Motor(port=Motor.PORT.B)
    b.reset()
    b.run_position_limited(60, 255, stop_mode=Motor.STOP_MODE.HOLD)

def distance():
    distance =  irsens.value()
    print "distance %s" % distance
    return distance

