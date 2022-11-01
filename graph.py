# Graph: An efficient graph.
# A graph implementation that uses an adjacency list to represent vertices
# and edges.
# Matthew Dyer

import functools

class Graph:
    def __init__(self):
        self.data = {}  

    def adjacent(self, vertA, vertB):
        return vertB in self.neighbors(vertA)

    def neighbors(self, vertex):
        if vertex in self.data:
            return self.data.get(vertex)
        else:
            return []

    def add_vertex(self, vertex):
        if vertex not in self.data:
            self.data[vertex] = []

    def remove_vertex(self, vertex):
        if vertex in self.data:
            for i in self.neighbors(vertex):
                self.neighbors(i).remove(vertex)
            self.data.pop(vertex)

    def add_edge(self, vertA, vertB):
        if vertA in self.data and vertB in self.data:
            if vertA not in self.data[vertB] and vertB not in self.data[vertA]:
                self.data[vertA].append(vertB)
                self.data[vertB].append(vertA)

    def remove_edge(self, vertA, vertB):
        if vertA in self.data and vertB in self.data:
            if vertA in self.data[vertB] and vertB in self.data[vertA]:
                self.neighbors(vertA).remove(vertB)
                self.neighbors(vertB).remove(vertA)

    def v(self):
        return len(self.data.keys())
    
    def e(self):
        sum = 0
        for key in self.data.keys():
            sum += len(self.data[key])
        return sum // 2