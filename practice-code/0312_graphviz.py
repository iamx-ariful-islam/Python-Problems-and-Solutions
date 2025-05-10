# pip install graphviz

from graphviz import Digraph


dot = Digraph()

dot.node('A', 'Start')
dot.node('B', 'Process')
dot.node('C', 'End')

dot.edges(['AB', 'BC'])
dot.render('flowchart', format='png', view=True)