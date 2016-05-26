# See http://ev3dev-lang.readthedocs.org/projects/python-ev3dev/en/stable/index.html
# for API details -- specific Sensor/Motor docs http://www.ev3dev.org/docs/
from time import sleep, time
from ev3dev.auto import *

# Connect two large motors on output ports A and C
lmotor, rmotor = [LargeMotor(address) for address in (OUTPUT_B, OUTPUT_D)]
moving = False

# Connect medium motors on output port B for the camera
cmotor = MediumMotor(OUTPUT_C)
camera_pos = 0
cmotor.reset()

# Check that the motors are actually connected
assert lmotor.connected
assert rmotor.connected

color_sensor = ColorSensor()
touch_sensor = TouchSensor()
gyro = GyroSensor()

speaking = None

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

def turn_right(speed=40):
    '''
    Turn while moving forward
    '''
    _start()
    lmotor.duty_cycle_sp=speed
    rmotor.duty_cycle_sp=0

def turn_left(speed=40):
    '''
    Turn while moving forward
    '''
    _start()
    lmotor.duty_cycle_sp=0
    rmotor.duty_cycle_sp=speed

def spin_right(speed=50):
    '''
    Turn on the spot
    '''
    _start()
    lmotor.duty_cycle_sp=speed
    rmotor.duty_cycle_sp=-speed

def spin_left(speed=50):
    '''
    Turn on the spot
    '''
    _start()
    lmotor.duty_cycle_sp=-speed
    rmotor.duty_cycle_sp=speed

def speak():
    global speaking
    print "%s" % speaking
    if speaking is None or time() - speaking > 1.6:
        speaking = time()
        print 'Excuse me!'
        Sound.speak('Excuse me!')

def light_green():
    Leds.set_color(Leds.LEFT+Leds.RIGHT, Leds.GREEN+Leds.GREEN)

def light_red():
    Leds.set_color(Leds.LEFT+Leds.RIGHT, Leds.RED+Leds.RED)

def color():
    return color_sensor.value()

def touch():
    return touch_sensor.value() == 1

def direction():
    return gyro.value() % 360  # degrees, but needs a 0 value

def camera_left():
    global camera_pos
    camera_pos -= 25
    camera_pos = max(-150, camera_pos)
    cmotor.run_to_abs_pos(speed_regulation_enabled='on', speed_sp=100, position_sp=camera_pos)

def camera_right():
    global camera_pos
    camera_pos += 25
    camera_pos = min(150, camera_pos)
    cmotor.run_to_abs_pos(speed_regulation_enabled='on', speed_sp=100, position_sp=camera_pos)

def camera_forward():
    global camera_pos
    camera_pos = 0
    cmotor.run_to_abs_pos(speed_regulation_enabled='on', speed_sp=100, position_sp=camera_pos)
