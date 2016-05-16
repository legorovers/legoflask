import threading
import time
import math
from Queue import Queue

class ControlThread(object):

    def __init__(self, delay=0):
        self.delay = delay
        self.queue = Queue()
        self.sleep = threading.Condition()

    def start(self, sense, rules, robot):
        self.sense = sense
        self.rules = rules
        self.robot = robot
        sense.start(self, robot)
        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True                            # Daemonize thread
        thread.start()                                  # Start the execution

    def operation(self, operation, args, delay_s=None):
        if delay_s is None:
            delay_s = self.delay / 1000.0
        self.queue.put({
            'operation': operation,
            'timestamp': time.time() + delay_s,
            'args': args
        })

    def readings(self, *args):
        self.rules.check(*args)
        self.queue.put({
            'operation': 'sensors',
            'timestamp': time.time(),
            'args': args
        })

    def program(self, *actions):
        self._drain_queue()
        for i in range(0, len(actions), 2):
            delay_s = actions[i]
            action = actions[i+1]
            self.operation('action', action, delay_s)
        self.sleep.acquire()
        self.sleep.notify()
        self.sleep.release()

    def _drain_queue(self):
        while not self.queue.empty():
            try:
                self.queue.get(False)
            except Empty:
                continue
            self.queue.task_done()

    def set_delay(self, delay):
        self._drain_queue()
        self.operation('action', (None, 0), 0)  # Stop everything!
        self.delay = delay

    def run(self):
        while True:
            task = self.queue.get()
            self.queue.task_done()
            delay_for = task['timestamp'] - time.time()
            #print "delay %s" % delay_for
            if delay_for > 0:
                self.sleep.acquire()
                self.sleep.wait(delay_for)
                self.sleep.release()
            op = task['operation']
            if op == 'action':
                self.action(*task['args'])
            elif op == 'camera':
                self.camera(*task['args'])
            elif op == 'sensors':
                self.sense.sensors(*task['args'])

    def action(self, direction, speed):
        print speed
        # scale quadratic, for easier control
        speed = math.sqrt(speed) * 7.0
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

