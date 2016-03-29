from time import sleep
from ev3dev.auto import *

# Connect two large motors on output ports B and C
lmotor, rmotor = [LargeMotor(address) for address in (OUTPUT_A, OUTPUT_B)]

# Check that the motors are actually connected
assert lmotor.connected
assert rmotor.connected

ussensor = UltrasonicSensor()

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
    for motor in (lmotor, rmotor):
        motor.run_timed(duty_cycle_sp=60, time_sp=500)

def backward():
    '''
    Reverse
    '''
    sleep(delay)
    for motor in (lmotor, rmotor):
        motor.run_timed(duty_cycle_sp=-60, time_sp=500)

def stop():
    '''
    Stop the robot
    '''
    sleep(delay)
    for motor in (lmotor, rmotor):
        motor.stop(stop_command='brake')

def spin_right():
    sleep(delay)
    lmotor.run_timed(duty_cycle_sp=60, time_sp=500)
    rmotor.run_timed(duty_cycle_sp=-60, time_sp=500)

def spin_left():
    sleep(delay)
    lmotor.run_timed(duty_cycle_sp=-60, time_sp=500)
    rmotor.run_timed(duty_cycle_sp=60, time_sp=500)

def distance():
    distance = ussensor.value() / 10.0
    print "distance %scm" % distance
    return distance

