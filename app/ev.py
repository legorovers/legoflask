from time import sleep
import ev3
from ev3.rawdevice import motordevice

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
    ev3.open_all_devices()
    motordevice.speed(both,20)
    sleep(0.3)
    motordevice.stop(both, brake=1)

def stop():
    '''
    Stop the robot
    '''
    pass
#    b = nxt.locator.find_one_brick()
#    m_left = Motor(b, PORT_B)
#    m_right = Motor(b, PORT_C)
#    m_left.idle()
#    m_right.idle()


def right():
    pass
#    b = nxt.locator.find_one_brick()
#    m_left = Motor(b, PORT_B)
#    m_right = Motor(b, PORT_C)
#    m_right.idle()
#    m_left.idle()
#    m_right.run(power=-100)
#    m_left.run(power=100)
#    sleep(0.3)
#    m_right.idle()
#    m_left.idle()

def left():
    pass
#    b = nxt.locator.find_one_brick()
#    m_left = Motor(b, PORT_B)
#    m_right = Motor(b, PORT_C)
#    m_left.run(power=-100)
#    m_right.run(power=-100)
#    sleep(0.5)
#    m_right.idle()
#    m_left.idle()
#    m_right.run(power=100)
#    m_left.run(power=-100)
#    sleep(0.7)
#    m_right.idle()
#    m_left.idle()
