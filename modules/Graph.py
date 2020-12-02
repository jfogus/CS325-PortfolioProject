# Author:  Joshua Fogus
# Course:  CS 325_400_F2020
# Date:  December 02, 2020
# Description:  Implements a graph of vertices and edges.

from Vertex import Vertex
from Edge import Edge


class Graph:
    def __init__(self, vertices, edges):
        self.__V = {(x, y): Vertex(x, y) for (x, y) in vertices}
        self.__E = [(self.__V[u], self.__V[v]) for (u, v) in edges]



if __name__ == "__main__":
    print("This is not meant to be run as a script. Please import this module.")