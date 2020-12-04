# Author:  Joshua Fogus
# Course:  CS 325_400_F2020
# Date:  December 03, 2020
# Description:  Tests for the Graph.py module.

import unittest
from Graph import Graph
from Edge import Edge
from Vertex import Vertex


class GraphTester(unittest.TestCase):
    def test_vertices(self):
        """ Tests that vertices are populated correctly on init. """
        v1 = Vertex(5, 3)
        v2 = Vertex(4, 2)
        v3 = Vertex(2, 8)
        v4 = Vertex(1, 9)
        v5 = Vertex(3, 1)
        v6 = Vertex(8, 6)
        e = Edge(v1, v2)
        f = Edge(v3, v4)
        g = Edge(v5, v6)

        graph = Graph({e, f, g})

        self.assertSetEqual(graph.vertices, {v1, v2, v3, v4, v5, v6})

    def test_edges(self):
        """ Tests that edges are populated correctly on init. """
        v1 = Vertex(5, 3)
        v2 = Vertex(4, 2)
        v3 = Vertex(2, 8)
        v4 = Vertex(1, 9)
        v5 = Vertex(3, 1)
        v6 = Vertex(8, 6)
        e = Edge(v1, v2)
        f = Edge(v3, v4)
        g = Edge(v5, v6)

        graph = Graph({e, f, g})

        self.assertSetEqual(graph.edges, {e, f, g})

    def test_adj_list(self):
        """ Tests that an adj list is populated correctly on init. """
        v1 = Vertex(5, 3)
        v2 = Vertex(4, 2)
        v3 = Vertex(2, 8)
        v4 = Vertex(1, 9)
        v5 = Vertex(3, 1)
        v6 = Vertex(8, 6)
        e = Edge(v1, v2)
        f = Edge(v3, v4)
        g = Edge(v5, v6)
        h = Edge(v1, v6)

        graph1 = Graph({e, f, g})
        graph2 = Graph({e, f, g, h})

        self.assertDictEqual(graph1.adj_list, {
            v1: {v2},
            v2: {v1},
            v3: {v4},
            v4: {v3},
            v5: {v6},
            v6: {v5}
        })
        self.assertDictEqual(graph2.adj_list, {
            v1: {v2, v6},
            v2: {v1},
            v3: {v4},
            v4: {v3},
            v5: {v6},
            v6: {v1, v5}
        })

    def test_get_len_connected(self):
        """ Tests that the number of connected vertices can be returned. """
        v1 = Vertex(5, 3)
        v2 = Vertex(4, 2)
        v3 = Vertex(2, 8)
        v4 = Vertex(1, 9)
        v5 = Vertex(3, 1)
        v6 = Vertex(8, 6)
        e = Edge(v1, v2)
        f = Edge(v5, v4)
        g = Edge(v5, v6)
        h = Edge(v1, v6)
        i = Edge(v6, v5)
        j = Edge(v5, v4)
        k = Edge(v3, v2)

        graph1 = Graph({e, f, g})
        graph2 = Graph({h, i, j, k})

        # Test singly connected vertex
        self.assertEqual(graph1.get_len_connected(v1), 2)
        # Test unconnected vertex
        self.assertEqual(graph1.get_len_connected(v3), 1)
        # Test multi-connected graph
        self.assertEqual(graph2.get_len_connected(v1), 4)
        # Test separate tree in multi-connected graph
        self.assertEqual(graph2.get_len_connected(v3), 2)

    def test_is_connected(self):
        """ Tests that connected graphs can properly be identified. """
        v1 = Vertex(5, 3)
        v2 = Vertex(4, 2)
        v3 = Vertex(2, 8)
        v4 = Vertex(1, 9)
        v5 = Vertex(3, 1)
        v6 = Vertex(8, 6)
        e = Edge(v1, v2)
        f = Edge(v5, v4)
        g = Edge(v5, v6)
        h = Edge(v1, v6)
        i = Edge(v6, v5)
        j = Edge(v5, v4)
        k = Edge(v4, v2)

        graph1 = Graph({e, f, g})
        graph2 = Graph({h, i, j, k})

        # Test disconnected graph
        self.assertFalse(graph1.is_connected())
        # Test connected graph
        self.assertTrue(graph2.is_connected())


if __name__ == "__main__":
    unittest.main()