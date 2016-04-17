import threading
import time
from Queue import Queue

class ControlThread(object):

    def __init__(self, delay=0):
        self.delay = delay
        self.queue = Queue()
        self.sleep = threading.Condition()

    def start(self, sense, robot):
        self.sense = sense
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
        self.rule_check(*args)
        self.queue.put({
            'operation': 'sensors',
            'timestamp': time.time(),
            'args': args
        })

    def rule_check(self, distance, touch_left, touch_right, direction):
        if distance == 0 or touch_left or touch_right:
            self._drain_queue()
            self.operation('action', ('reverse', 40), 0)
            self.operation('action', ('stop', None), 0.5)
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
        self.operation('action', ('stop', None), 0)
        self.delay = delay

    def run(self):
        while True:
            task = self.queue.get()
            self.queue.task_done()
            delay_for = task['timestamp'] - time.time()
            print "delay %s" % delay_for
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

