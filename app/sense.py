import threading
import time

class SensorThread(object):

    def __init__(self, notify, delay=0):
        self.notify = notify
        self.delay = delay
        self.interval = 1
        self.distance = -1

    def start(self, robot):
        self.robot = robot
        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True                            # Daemonize thread
        thread.start()                                  # Start the execution

    def run(self):
        while True:
            distance = int(self.robot.distance())
            if not self.distance == distance:
                self.notify.emit('sense', distance)
                self.distance = distance
                print "distance %scm" % distance
            time.sleep(self.interval)
