KISS state machine under 50 LOC for micropython use
---------------------------------------------------

# Example:
_it's in the dumb_test.py__

``` py
from USM import *

if __name__ == '__main__':
    class TestModel():
        def __init__(self):
            self.superb = 1
    model = TestModel()
    transitions = [
            Transition('A','B','C', lambda x: print("lol")),
            Transition('C','B','D', lambda x: print("passed condition"), lambda x: x.superb == 1),
            Transition('D','B','D', lambda x: print("condition not passed"), lambda x: x.superb == 0)
            ]
    m = Machine(model, transitions, 'A')
    m.dispatch('B')
    m.dispatch('B')
    m.dispatch('B')
    print("curent state is: %s"%(m.curent))
```

will result in output:
```
A -> C
lol
C -> D
passed condition
curent state is: D
```

This SM follows aproach:
_Event triggers change of state depending on conditional which results in state change callback_

Due to size there are some limitations:
1. _there are no pre/post state callbacks_
2. _state change will always result in first match_
3. _if there is no match - it will do nothing_
4. _it's flat_

My goal was to create something as small as possible under an hour, and here it is :)

# TL;DR;

## So how it works

As state machine use is pretty similar to any other state machine implementation it should be pretty straightforward to use.
But if it's not, here is some extended documentation:

The base of state machine is a list of transitions, a transition consist of:
- entry state
- transmission triggering event
- end state
which are mandatory, as well as:
- callback
- guard
which are non mandatory

in our example:
``` py
    transitions = [
            Transition('C','B','D', lambda x: print("passed condition"), lambda x: x.superb == 1),
            ]
```
Transmission is defined as:

State `C` enters State `D` on event `B` on condition `lambda x: x.superb` if it does - it triggers `lambda x: ("passed condition)`

What might be confusing is `x.superb` : from where does the `superb` come from?

It comes from the Model, to be exact from:
``` py
    class TestModel():
        def __init__(self):
            self.superb = 1
```

## So what are my transitions

Just follow `graph.py`

# Notes:
- I may add a bit extended version of that if I need it
- **Code under Beerware license, use on your own responsibility**
