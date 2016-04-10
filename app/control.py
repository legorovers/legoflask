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

    def operation(self, operation, args):
        self.queue.put({
            'operation': operation,
            'timestamp': time.time(),
            'args': args
        })

    def run(self):
        while True:
            task = self.queue.get()
            self.queue.task_done()
            if self.delay > 0:
                delay_for = (task['timestamp'] + self.delay / 1000.0) - time.time()
                if delay_for > 0:
                    time.sleep(delay_for)
            op = task['operation']
            if op == 'action':
                self.action(*task['args'])
            elif op == 'camera':
                self.camera(*task['args'])

    def action(self, direction, speed):
        print speed
        # clamp to valid values
        speed = min(100, max(25, speed))
        if direction == 'forward':
            self.robot.forward(speed)
        elif direction == 'left':
            self.robot.spin_left(speed)
        elif direction == 'right':
            self.robot.spin_right(speed)
        elif direction == 'reverse':
            self.robot.backward(speed)
        else:
            self.robot.stop()

    def camera(self, direction):
        if direction == 'left':
            self.robot.camera_left()
        elif direction == 'right':
            self.robot.camera_right()
        else:
            self.robot.camera_forward()

