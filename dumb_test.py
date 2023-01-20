from USM import *

transitions = [
        Transition('A','B','C', lambda x: print("lol")),
        Transition('C','B','D', lambda x: print("passed condition"), lambda x: x.superb == 1),
        Transition('D','B','D', lambda x: print("condition not passed"), lambda x: x.superb == 0)
        ]


if __name__ == '__main__':
    class TestModel():
        def __init__(self):
            self.superb = 1

    model = TestModel()
    m = Machine(model, transitions, 'A')
    m.dispatch('B')
    m.dispatch('B')
    m.dispatch('B')
    print("curent state is: %s"%(m.curent))

