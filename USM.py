# Code under Beerware license, use on your own responsibility
class Error(RuntimeError):
    pass


class Transition():
    def __init__(self, entry, trigger, result, callback=lambda x: None, condition=lambda x: True):
        self.entry = entry
        self.result = result
        self.trigger = trigger
        self.callback = callback
        self.condition = condition
        if self.entry is None or self.result is None:
            raise Error('invalid transition, none state')

    def transmit(self, event, model):
        if event == self.trigger and self.condition(model):
            print('%s -> %s' % (self.entry, self.result))
            self.callback(model)
            return True
        return False

    def start(self):
        return self.entry


class Machine():
    def __init__(self, model, transitions, initial):
        self.model = model
        self.transitions = transitions
        self.curent = initial

    def dispatch(self, event):
        for t in self.transitions:
            if t.start() != self.curent:
                continue
            if t.transmit(event, self.model):
                self.curent = t.result
                return
