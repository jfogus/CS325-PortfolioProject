# Author:  Joshua Fogus
# Course:  CS 325_400_F2020
# Date:  December 02, 2020
# Description:  Tests for the Queue.py module.

import unittest
from Queue import Queue


class QueueTester(unittest.TestCase):
    def test_enqueue(self):
        """ Tests enqueue values. """
        queue = Queue()
        queue.enqueue(5)
        queue.enqueue(7)
        queue.enqueue(11)

        self.assertEqual(queue.__str__(), "{}".format([5, 7, 11]))

    def test_dequeue(self):
        """ Tests dequeueing values. """
        queue = Queue()
        queue.enqueue(5)
        queue.enqueue(7)
        queue.enqueue(11)

        self.assertEqual(queue.dequeue(), 5)
        self.assertEqual(queue.dequeue(), 7)

        queue.enqueue(13)

        self.assertEqual(queue.dequeue(), 11)
        self.assertEqual(queue.dequeue(), 13)

    def test_length(self):
        """ Tests returning the length of the queue. """
        queue = Queue()
        queue.enqueue(5)

        self.assertEqual(queue.length(), 1)

        queue.enqueue(7)
        queue.enqueue(11)
        self.assertEqual(queue.length(), 3)

        queue.dequeue()
        queue.dequeue()
        queue.dequeue()
        self.assertEqual(queue.length(), 0)


if __name__ == "__main__":
    unittest.main()
