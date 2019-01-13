# Implementing an Graph in python using adjacency list

# A - C - D
#  \ /
#   B


class Graph():

    def __init__(self):
        self.graph = {}

    def add_node(self, val, vertex):
        self.graph[val] = vertex

    def __repr__(self):
        return "Graph(%s)" % self.graph


graph = Graph()
print(graph)
graph.add_node('A', ['B', 'C'])
graph.add_node('B', ['A', 'C'])
graph.add_node('C', ['A', 'B', 'D'])
print(graph)
