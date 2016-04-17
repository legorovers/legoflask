

class RuleEngine(object):

    def __init__(self, control):
        self.control = control

    def check(self, distance, touch_left, touch_right, direction):
        if distance == 0 or touch_left or touch_right:
            self.control.program(*self.code)

    def compile(self, trigger, actions):
        self.trigger = trigger
        print "trigger: %s" % trigger
        self.code = []
        time = 0
        for a in actions:
            print "action: %s" % a
            if a == 'back':
                action = ('reverse', 40)
            elif a == 'stop':
                action = ('stop', None)
            else:   # forward, left, right
                action = (a, 40)
            self.code.append(time)
            self.code.append(action)
            time += 0.5
        print "code: %s" % self.code
