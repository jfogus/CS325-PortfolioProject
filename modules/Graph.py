# Author:  Joshua Fogus
# Course:  CS 325_400_F2020
# Date:  December 03, 2020
# Description:  Implements a graph of vertices and edges.

from Vertex import Vertex
from Edge import Edge
from Queue import Queue
from copy import deepcopy


class Graph:
    """ Given a set of edges (pairs of vertices), constructs a graph with an
        adjacency list. """
    def __init__(self, edges):
        self.__edges = set(edges)
        self.__vertices = set()
        self.__adj_list = dict()

        # Add vertices and populate adjacency list from edges
        for edge in self.__edges:
            self.__vertices.add(edge.u)
            self.__vertices.add(edge.v)

            try:
                self.__adj_list[edge.u].append(edge.v)
            except KeyError:
                self.__adj_list[edge.u] = [edge.v]

            try:
                self.__adj_list[edge.v].append(edge.u)
            except KeyError:
                self.__adj_list[edge.v] = [edge.u]

    @property
    def vertices(self):
        return self.__vertices

    @property
    def edges(self):
        return self.__edges

    def is_connected(self):
        """ Returns true if all vertices in the graph are reachable from
            all other vertices in the graph. Otherwise returns False. O(V + E) """
        return len(self.__vertices) == self.get_len_connected()

    def get_len_connected(self):
        """ Uses BFS from an arbitrary source vertex and returns the number
            of nodes reachable from that source including itself as
            an integer. O(V + E) """
        vertices = deepcopy(self.__vertices)
        count = 0

        queue = Queue()
        queue.enqueue(vertices.pop())

        for vertex in vertices:
            vertex.visited = False

        while queue.length != 0:
            u = queue.dequeue()
            count += 1

            for v in self.__adj_list[u]:
                v.visited = True
                queue.enqueue(v)

        return count


if __name__ == "__main__":
    print("This is not meant to be run as a script. Please import this module.")