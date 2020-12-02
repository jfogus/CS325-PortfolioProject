# Author:  Joshua Fogus
# Course:  CS 325_400_F2020
# Date:  December 02, 2020
# Description:  Tests for the Vertex.py module.

import unittest
from Vertex import Vertex

class VertexTester(unittest.TestCase):
    def test_get_x(self):
        """ Tests getting an x coordinate. """
        v = Vertex(2, 5)

        self.assertEqual(v.x, 2)

    def test_get_y(self):
        """ Tests getting a y coordinate. """
        v = Vertex(3, 9)

        self.assertEqual(v.y, 9)

    def test_get_coords(self):
        """ Tests getting complete coordinates. """
        v = Vertex(7, 1)

        self.assertTupleEqual(v.coords, (7, 1))


if __name__ == "__main__":
    unittest.main()