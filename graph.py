import graphviz
from dumb_test import transitions

dot = graphviz.Digraph(comment='The Round Table')
nodes = []
for t in transitions:
    s = t.entry
    e = t.result
    def add(a,dot,nodes):
        if a not in nodes:
            print(f'add {a}')
            dot.node(a,a)
            nodes += [a]
    add(s, dot,nodes)
    add(e, dot,nodes)
    print(f'add: {s} -> {e}')
    dot.edge(s,e,constraint='false')
print('graph printed: enjoy')
dot.render('doc/test.gv', view=True)
