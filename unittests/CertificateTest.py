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
            Vertex(3, 5): 4
        })

        e = Edge(Vertex(3, 3), Vertex(3, 7))
        f = Edge(Vertex(1, 5), Vertex(5, 5))
        g = Edge(Vertex(2, 4), Vertex(4, 6))
        h = Edge(Vertex(1, 9), Vertex(5, 9))
        i = Edge(Vertex(3, 4), Vertex(3, 6))
        j = Edge(Vertex(2, 5), Vertex(7, 5))

        # Valid horizontal edge
        c.add_edge(e.u, e.v)
        # Valid vertical edge
        c.add_edge(f.u, f.v)
        # Invalid diagonal edge
        c.add_edge(g.u, g.v)
        # Invalid non-intersected edge
        c.add_edge(h.u, h.v)
        # Invalid short length
        c.add_edge(i.u, i.v)
        # Invalid long length
        c.add_edge(j.u, j.v)

        self.assertSetEqual(set(c.edges.keys()), {
            (e.u, e.v),
            (f.u, f.v)
        })

    def test_remove_edge(self):
        """ Tests removing an edge from the certificate. """
        c = Certificate({
            Vertex(3, 5): 4
        })

        e = Edge(Vertex(3, 3), Vertex(3, 7))
        f = Edge(Vertex(1, 5), Vertex(5, 5))
        c.add_edge(e.u, e.v)

        # Existent edge
        c.remove_edge(e.u, e.v)
        # Nonexistent edge
        c.remove_edge(f.u, f.v)

        self.assertEqual(len(c.edges), 0)

    def test_validate_edge(self):
        """ Tests that an edge meets the condition that intersects it. """
        c = Certificate({
            Vertex(3, 5): 4
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
            Vertex(1, 0): 3,
            Vertex(2, 1): 4,
            Vertex(1, 3): 2
        })

        e = Edge(Vertex(0, 0), Vertex(3, 0))
        f = Edge(Vertex(2, 0), Vertex(2, 4))
        g = Edge(Vertex(0, 3), Vertex(2, 3))

        c.add_edge(e.u, e.v)
        c.add_edge(f.u, f.v)
        c.add_edge(g.u, g.v)

        graph = c.get_graph()

        self.assertEqual(len(graph.edges), 5)


if __name__ == "__main__":
    unittest.main()