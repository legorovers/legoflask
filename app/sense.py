import threading
import time

class SensorThread(object):

    def __init__(self, robot, notify, delay=0):
        self.robot = robot
        self.notify = notify
        self.delay = delay
        self.interval = 1

        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True                            # Daemonize thread
        thread.start()                                  # Start the execution

    def run(self):
        while True:
            distance = self.robot.distance()
            self.notify.emit('sense', distance)
            time.sleep(self.interval)
