import threading
import time

class SensorThread(object):

    def __init__(self, notify, delay=0):
        self.notify = notify
        self.delay = delay
        self.interval = 0.1
        self.color = -1

    def start(self, control, robot):
        self.control = control
        self.robot = robot
        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True                            # Daemonize thread
        thread.start()                                  # Start the execution

    def run(self):
        while True:
            color = int(self.robot.color())
            touch = self.robot.touch()
            try:
                direction = self.robot.direction()
            except:
                direction = 0
            self.control.readings(color, touch, direction)
            time.sleep(self.interval)

    def sensors(self, color, touch, direction):
        #print "sense: %s %s" % (touch, direction)
        if not self.color == color:
            self.notify.emit('sense', color)
            self.color = color
            print "color %s%%" % color
