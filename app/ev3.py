# See http://ev3dev-lang.readthedocs.org/projects/python-ev3dev/en/stable/index.html
# for API details -- specific Sensor/Motor docs http://www.ev3dev.org/docs/
from time import sleep
from ev3dev.auto import *

# Connect two large motors on output ports A and C
lmotor, rmotor = [LargeMotor(address) for address in (OUTPUT_A, OUTPUT_C)]
moving = False

# Check that the motors are actually connected
assert lmotor.connected
assert rmotor.connected

ussensor = UltrasonicSensor()

def _start():
    '''
    Start the motors using run_direct() so we can just vary speed
    '''
    global moving
    if not moving:
        for motor in (lmotor, rmotor):
            motor.duty_cycle_sp = 0
            motor.run_direct()
        moving = True

def forward(speed=50):
    '''
    Move the robot forward
    '''
    _start()
    for motor in (lmotor, rmotor):
        motor.duty_cycle_sp=speed

def backward(speed=50):
    '''
    Reverse
    '''
    _start()
    for motor in (lmotor, rmotor):
        motor.duty_cycle_sp=-speed

def stop():
    '''
    Stop the robot
    '''
    global moving
    for motor in (lmotor, rmotor):
        motor.stop()
    moving = False

def spin_right(speed=50):
    _start()
    lmotor.duty_cycle_sp=speed
    rmotor.duty_cycle_sp=-speed

def spin_left(speed=50):
    _start()
    lmotor.duty_cycle_sp=-speed
    rmotor.duty_cycle_sp=speed

def distance():
    return ussensor.value() / 10.0

