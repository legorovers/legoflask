import threading
import time

class SensorThread(object):

    def __init__(self, notify, delay=0):
        self.notify = notify
        self.delay = delay
        self.interval = 0.2
        self.distance = -1

    def start(self, control, robot):
        self.control = control
        self.robot = robot
        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True                            # Daemonize thread
        thread.start()                                  # Start the execution

    def run(self):
        while True:
            distance = int(self.robot.distance())
            touch_left = self.robot.touch_left()
            touch_right = self.robot.touch_right()
            direction = self.robot.direction()
            self.control.readings(distance, touch_left, touch_right, direction)
            time.sleep(self.interval)

    def sensors(self, distance, touch_left, touch_right, direction):
        print "sense: %s %s %s" % (touch_left, touch_right, direction)
        if not self.distance == distance:
            self.notify.emit('sense', distance)
            self.distance = distance
            print "distance %scm" % distance
