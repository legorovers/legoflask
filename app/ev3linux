from time import sleep
#from ev3.rawdevice import motordevice
#from ev3.rawdevice import analogdevice
#from ev3.rawdevice import uartdevice
#from ev3.sensor import lego
from ev3.ev3dev import Motor

#motordevice.open_device()
#analogdevice.open_device()
#uartdevice.open_device() 

A = 0x01
B = 0x02
C = 0x04
D = 0x08

right = A
left = B
both = A+B

def forward():
    '''
    Move the robot forward
    '''
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
    motordevice.stop(both, brake=1)

def spin_right():
    a=Motor(port=Motor.PORT.A)
    a.reset()
    a.run_position_limited(30, 255, stop_mode=Motor.STOP_MODE.HOLD)
    b=Motor(port=Motor.PORT.B)
    b.reset()
    b.run_position_limited(-30, 255, stop_mode=Motor.STOP_MODE.HOLD)

def spin_left():
    a=Motor(port=Motor.PORT.A)
    a.reset()
    a.run_position_limited(-30, 255, stop_mode=Motor.STOP_MODE.HOLD)
    b=Motor(port=Motor.PORT.B)
    b.reset()
    b.run_position_limited(30, 255, stop_mode=Motor.STOP_MODE.HOLD)

def distance():
    return 1
