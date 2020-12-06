# Author:  Joshua Fogus
# Course:  CS 325_400_F2020
# Date:  December 04, 2020
# Description:  Implements an certificate for the problem to be tested as a solution.

from Edge import Edge
from Vertex import Vertex
from Graph import Graph


class Certificate:
    """ Accepts a set of conditions in the form of {(x, y): integer}, where
        integer is the requirement. Collects proposed edges for a solution. """
    def __init__(self, conditions):
        self.__edges = {}
        self.__conditions = {Vertex(coords[0], coords[1]): value for coords, value in conditions.items()}

    @property
    def edges(self):
        return self.__edges

    def add_edge(self, u_coords, v_coords):
        """ Adds a valid edge to the set of edges in the certificate and returns
            True if added. Otherwise returns False. O(C) """
        u = Vertex(u_coords[0], u_coords[1])
        v = Vertex(v_coords[0], v_coords[1])
        edge = Edge(u, v)

        if self.validate_edge(edge):
            self.__edges[u, v] = edge
            return True

        return False

    def remove_edge(self, u, v):
        """ Removes an edge from the set of edges in the certificate, given
            coordinates for the edges vertices as tuples in the form (x, y). """
        for key, edge in self.__edges.items():
            if edge.u.x == u[0] and edge.u.y == u[1] and edge.v.x == v[0] and edge.v.y == v[1]:
                del self.__edges[key]
                return

    def validate_edge(self, edge):
        """ Confirms that an edge meets one of the conditions, returning True if
            it does and False otherwise. O(C) per run. For a valid certificate
            it will be run E times yielding O(E*C). """
        for vertex, condition in self.__conditions.items():
            if edge.is_intersected_by(vertex) \
                    and edge.get_length() == condition\
                    and (edge.get_slope() == 0 or edge.get_slope() is None):
                return True

        return False

    def get_graph(self):
        """ Returns a set of edges that can be used to create a graph. Edges that
            are bisected by vertices of other edges are removed and replaced by
            two equivalent edges. O(E*V) """
        edges = set()
        vertices = set()

        for edge in self.__edges.values():
            vertices.add(edge.u)
            vertices.add(edge.v)

        # If an edge is intersected by a vertex, replace the edge with the two
        # edges created by the intersection and remove the original edge
        for edge in self.__edges.values():
            split = False

            for vertex in vertices:
                # TODO: handle if a vertex is intersected by multiple vertices
                if edge.is_intersected_by(vertex) and edge.u is not vertex and edge.v is not vertex:
                    edges.add(Edge(edge.u, vertex))
                    edges.add(Edge(vertex, edge.v))
                    split = True

            # There was no intersecting vertex
            if split is False:
                edges.add(edge)

        return Graph(edges)


if __name__ == "__main__":
    print("This is not meant to be run as a script. Please import this module.")