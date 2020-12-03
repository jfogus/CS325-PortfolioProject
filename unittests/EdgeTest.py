# Author:  Joshua Fogus
# Course:  CS 325_400_F2020
# Date:  December 03, 2020
# Description:  Tests for the Edge.py module.

import unittest
from Edge import Edge
from Vertex import Vertex


class EdgeTester(unittest.TestCase):
    def test_is_valid_length(self):
        """ Tests determining if an edge length is valid given
            a requirement. """
        e = Edge(Vertex(5, 4), Vertex(5, 1))
        f = Edge(Vertex(5, 3), Vertex(3, 3))
        g = Edge(Vertex(5, 3), Vertex(5, 9))
        h = Edge(Vertex(5, 5), Vertex(5, 4))

        # Test length below requirement
        self.assertFalse(e.is_valid_length(2))
        # Test length above requirement
        self.assertFalse(f.is_valid_length(3))
        # Test correct length
        self.assertTrue(g.is_valid_length(6))
        # Test length < 2
        self.assertFalse(h.is_valid_length(1))

    def test_get_length(self):
        """ Tests getting the length of an edge. """
        e = Edge(Vertex(5, 4), Vertex(5, 1))
        f = Edge(Vertex(5, 3), Vertex(3, 3))
        g = Edge(Vertex(5, 3), Vertex(5, 9))
        h = Edge(Vertex(5, 5), Vertex(8, 9))

        # Test vertical
        self.assertEqual(e.get_length(), 3)
        # Test horizontal
        self.assertEqual(f.get_length(), 2)
        # Test negative difference
        self.assertEqual(g.get_length(), 6)
        # Test non-aligned
        self.assertEqual(h.get_length(), 7)

    def test_is_aligned(self):
        """ Tests determining alignment of vertices in an edge. """
        e = Edge(Vertex(5, 4), Vertex(5, 1))
        f = Edge(Vertex(5, 3), Vertex(3, 3))
        g = Edge(Vertex(5, 5), Vertex(8, 9))

        # Test vertical
        self.assertTrue(e.is_aligned())
        # Test horizontal
        self.assertTrue(f.is_aligned())
        # Test non-aligned
        self.assertFalse(g.is_aligned())

    def test_get_slope(self):
        """ Tests calculation of edge slope. """
        e = Edge(Vertex(5, 4), Vertex(5, 1))
        f = Edge(Vertex(5, 3), Vertex(3, 3))
        g = Edge(Vertex(3, 3), Vertex(5, 5))
        h = Edge(Vertex(3, 3), Vertex(5, 1))

        # Test vertical
        self.assertIsNone(e.get_slope())
        # Test horizontal
        self.assertEqual(f.get_slope(), 0)
        # Test positive, diagonal slope
        self.assertEqual(g.get_slope(), 1)
        # Test negative, diagonal slope
        self.assertEqual(h.get_slope(), -1)

    def test_is_intersected_by(self):
        """ Tests if vertices can be identified as intersecting an edge. """
        e = Edge(Vertex(3, 3), Vertex(5, 1))

        # Test vertex does not intersect
        self.assertFalse(e.is_intersected_by(Vertex(6, 6)))
        # Test vertex does intersect
        self.assertTrue(e.is_intersected_by(Vertex(4, 2)))
        # Test vertex with equal slopes but with x too great
        self.assertFalse(e.is_intersected_by(Vertex(6, 0)))
        # Test vertex with equal slopes but with x too small
        self.assertFalse(e.is_intersected_by(Vertex(2, 4)))
        # Test vertex equal to u
        self.assertTrue(e.is_intersected_by(Vertex(3, 3)))
        # Test vertex equal to v
        self.assertTrue(e.is_intersected_by(Vertex(5, 1)))


if __name__ == "__main__":
    unittest.main()