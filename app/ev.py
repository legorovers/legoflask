from time import sleep
import ev3
from ev3.rawdevice import motordevice

ev3.open_all_devices()

A = 0x01
B = 0x02
C = 0x04
D = 0x08

right = B
left = C
both = B+C

def forward():
    '''
    Move the robot forward
    '''
    motordevice.speed(both,20)
    sleep(0.3)
    motordevice.stop(both, brake=1)

def backward():
    '''
    Reverse
    '''
    motordevice.polarity(both,0)
    motordevice.speed(both,20)
    sleep(0.3)
    motordevice.stop(both, brake=1)
    motordevice.polarity(both,0)

def stop():
    '''
    Stop the robot
    '''
    motordevice.stop(both, brake=1)

def spin_right():
    motordevice.polarity(left,0)
    motordevice.speed(both,20)
    sleep(0.3)
    motordevice.stop(both, brake=1)
    motordevice.polarity(left,0)

def spin_left():
    motordevice.polarity(right,0)
    motordevice.speed(both,20)
    sleep(0.3)
    motordevice.stop(both, brake=1)
    motordevice.polarity(right,0)
