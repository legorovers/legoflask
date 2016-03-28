import threading
import time

class RobotThread(object):

    def __init__(self, delay=1):
        """ Constructor
        :type interval: int
        :param interval: Check interval, in seconds
        """
        self.delay = delay

        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True                            # Daemonize thread
        thread.start()                                  # Start the execution

    def run(self):
        """ Method that runs forever """
        while True:
            # Do something
            print('Doing something imporant in the background')

            time.sleep(self.delay)
