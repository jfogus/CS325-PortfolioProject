# Author:  Joshua Fogus
# Course:  CS 325_400_F2020
# Date:  December 04, 2020
# Description:  Implements an certificate for the problem to be tested as a solution.

from Edge import Edge


class Certificate:
    """ Accepts a set of conditions in the form of {Vertex: integer}, where
        the vertex corresponds to the coordinates of a condition and the
        integer is the requirement. Collects proposed edges for a solution. """
    def __init__(self, conditions):
        self.__edges = {}
        self.__conditions = conditions

    def add_edge(self, u, v):
        """ Adds a valid edge to the set of edges in the certificate and returns
            True if added. Otherwise returns False. O(C) """
        edge = Edge(u, v)

        if self.validate_edge(edge):
            self.__edges[u, v] = edge
            return True

        return False

    def remove_edge(self, u, v):
        """ Removes an edge from the set of edges in the certificate"""
        del self.__edges[u, v]

    def validate_edge(self, edge):
        """ Confirms that an edge meets one of the conditions, returning True if
            it does and False otherwise. O(C) per run. For a valid certificate
            it will be run E times yielding O(E*C). """
        for vertex, condition in self.__conditions.items():
            if edge.is_intersected_by(vertex) and edge.get_length() == condition:
                return True

        return False

    def get_graph_edges(self):
        """ Returns a set of edges that can be used to create a graph. Edges that
            are bisected by vertices of other edges are removed and replaced by
            two equivalent edges. O(E*V) """
        pass



if __name__ == "__main__":
    print("This is not meant to be run as a script. Please import this module.")