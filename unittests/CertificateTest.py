# Author:  Joshua Fogus
# Course:  CS 325_400_F2020
# Date:  December 04, 2020
# Description:  Tests for the Certificate.py module.

import unittest
from Certificate import Certificate
from Edge import Edge
from Vertex import Vertex


class CertificateTester(unittest.TestCase):
    def test_add_edge(self):
        """ Tests adding an edge to the certificate. """
        c = Certificate({
            (3, 5): 4
        })

        e = ((3, 3), (3, 7))
        f = ((1, 5), (5, 5))
        g = ((2, 4), (4, 6))
        h = ((1, 9), (5, 9))
        i = ((3, 4), (3, 6))
        j = ((2, 5), (7, 5))

        # Valid horizontal edge
        c.add_edge(e[0], e[1])
        # Valid vertical edge
        c.add_edge(f[0], f[1])
        # Invalid diagonal edge
        c.add_edge(g[0], g[1])
        # Invalid non-intersected edge
        c.add_edge(h[0], h[1])
        # Invalid short length
        c.add_edge(i[0], i[1])
        # Invalid long length
        c.add_edge(j[0], j[1])

        self.assertEqual(len(set(c.edges.keys())), 2)

    def test_remove_edge(self):
        """ Tests removing an edge from the certificate. """
        c = Certificate({
            (3, 5): 4
        })

        e = Edge(Vertex(3, 3), Vertex(3, 7))
        f = Edge(Vertex(1, 5), Vertex(5, 5))
        c.add_edge((3, 3), (3, 7))

        # Existent edge
        c.remove_edge((3, 3), (3, 7))
        # Nonexistent edge
        c.remove_edge((1, 5), (5, 5))

        self.assertEqual(len(c.edges), 0)

    def test_validate_edge(self):
        """ Tests that an edge meets the condition that intersects it. """
        c = Certificate({
            (3, 5): 4
        })

        e = Edge(Vertex(3, 3), Vertex(3, 7))
        f = Edge(Vertex(1, 5), Vertex(5, 5))
        g = Edge(Vertex(1, 3), Vertex(5, 7))
        h = Edge(Vertex(1, 9), Vertex(5, 11))

        # Valid horizontal edge
        self.assertTrue(c.validate_edge(e))
        # Valid vertical edge
        self.assertTrue(c.validate_edge(f))
        # Invalid diagonal edge
        self.assertFalse(c.validate_edge(g))
        # Invalid non-intersected edge
        self.assertFalse(c.validate_edge(h))

    def test_get_graph(self):
        """ Tests that a graph can be made from disconnected edges. """
        c = Certificate({
            (1, 0): 3,
            (2, 1): 4,
            (1, 3): 2
        })

        e = ((0, 0), (3, 0))
        f = ((2, 0), (2, 4))
        g = ((0, 3), (2, 3))

        c.add_edge(e[0], e[1])
        c.add_edge(f[0], f[1])
        c.add_edge(g[0], g[1])

        graph = c.get_graph()

        self.assertEqual(len(graph.edges), 5)


if __name__ == "__main__":
    unittest.main()