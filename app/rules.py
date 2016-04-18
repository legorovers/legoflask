

class Rule(object):

    def __init__(self, trigger, actions):
        self.trigger = trigger
        print "trigger: %s" % trigger
        self.code = []
        time = 0
        for a in actions:
            print "action: %s" % a
            if a == 'back':
                action = ('reverse', 40)
            elif a == 'stop':
                action = (None, 0)
            else:   # forward, left, right
                action = (a, 40)
            self.code.append(time)
            self.code.append(action)
            time += 0.5
        print "code: %s" % self.code

class RuleEngine(object):

    def __init__(self, control):
        self.control = control
        self.rules = []

    def check(self, distance, touch_left, touch_right, direction):
        for rule in self.rules:
            if (rule.trigger == 'left obstacle' and touch_left) \
                   or (rule.trigger == 'right obstacle' and touch_right) \
                   or (rule.trigger == 'proximity' and distance < 8):
                self.control.program(*rule.code)

    def activate(self, rules):
        self.rules = rules
