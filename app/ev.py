from time import sleep
from ev3.rawdevice import motordevice
#from ev3.rawdevice import analogdevice
from ev3.rawdevice import uartdevice
from ev3.sensor import lego

motordevice.open_device()
#analogdevice.open_device()
uartdevice.open_device() 

A = 0x01
B = 0x02
C = 0x04
D = 0x08

right = B
left = C
both = B+C

ir = lego.EV3IRSensor(2)  # looks like a 0-based count
ir.set_proximity_mode()

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

def distance():
    return ir.get_distance()

