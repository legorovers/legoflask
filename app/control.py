import threading
import time
from Queue import Queue

class ControlThread(object):

    def __init__(self, delay=0):
        self.delay = delay
        self.queue = Queue()

    def start(self, robot):
        self.robot = robot
        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True                            # Daemonize thread
        thread.start()                                  # Start the execution

    def run(self):
        while True:
            task = self.queue.get()
            if self.delay > 0:
                time.sleep(self.delay / 1000)
            self.action(*task)
            self.queue.task_done()

    def action(self, direction, speed):
        print speed
        if direction == 'forward':
            self.robot.forward()
        elif direction == 'left':
            self.robot.spin_left()
        elif direction == 'right':
            self.robot.spin_right()
        elif direction == 'reverse':
            self.robot.backward()
        else:
            self.robot.stop()
