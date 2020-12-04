# Author:  Joshua Fogus
# Course:  CS 325_400_F2020
# Date:  December 02, 2020
# Description:  Tests for the DoublyLinkedList.py module.

import unittest
from DoublyLinkedList import DoublyLinkedList
from DoublyLinkedList import Node


class NodeTester(unittest.TestCase):
    def test_get_val(self):
        """ Tests retrieval of a value from a node. """
        n = Node(5)

        self.assertEqual(n.val, 5)

    def test_set_val(self):
        """ Tests setting a value on a node. """
        n = Node(5)
        n.val = 9

        self.assertEqual(n.val, 9)

    def test_get_next_empty(self):
        """ Tests retrieval of next node when empty. """
        n = Node(5)

        self.assertIsNone(n.next)

    def test_set_next(self):
        """ Tests setting the next node. """
        m = Node(5)
        n = Node(7)
        m.next = n

        self.assertIsNotNone(m.next)

    def test_get_next(self):
        """ Tests retrieval of next node when not empty. """
        m = Node(5)
        n = Node(7)
        m.next = n

        self.assertIs(m.next, n)

    def test_get_prev_empty(self):
        """ Tests retrieval of prev node when empty. """
        n = Node(5)

        self.assertIsNone(n.prev)

    def test_set_prev(self):
        """ Tests setting the prev node. """
        m = Node(5)
        n = Node(7)
        n.prev = m

        self.assertIsNotNone(n.prev)

    def test_get_prev(self):
        """ Tests retrieval of prev node when not empty. """
        m = Node(5)
        n = Node(7)
        n.prev = m

        self.assertIs(n.prev, m)


class DoublyLinkedListTester(unittest.TestCase):
    def test_get_sentinel(self):
        """ Tests retrieval of DLL sentinel. """
        dll = DoublyLinkedList()

        self.assertIsNone(dll.sentinel.val)

    def test_append(self):
        """ Tests appending a node to DLL. """
        dll = DoublyLinkedList()
        dll.append(5)
        dll.append(7)
        dll.append(11)

        self.assertEqual(dll.__str__(), "[5, 7, 11]")

    def test_prepend(self):
        """ Tests prepending a node to DLL. """
        dll = DoublyLinkedList()
        dll.append(5)
        dll.append(7)
        dll.prepend(3)

        self.assertEqual(dll.__str__(), "[3, 5, 7]")

    def test_remove_first(self):
        """ Tests removing the first node in DLL. """
        dll = DoublyLinkedList()
        dll.append(5)
        dll.append(7)
        dll.append(11)

        self.assertEqual(dll.remove_first(), 5)
        self.assertEqual(dll.__str__(), "[7, 11]")
        self.assertEqual(dll.remove_first(), 7)
        self.assertEqual(dll.remove_first(), 11)
        self.assertIsNone(dll.remove_first())

    def test_remove_last(self):
        """ Tests removing the last node in DLL. """
        dll = DoublyLinkedList()
        dll.append(5)
        dll.append(7)
        dll.append(11)

        self.assertEqual(dll.remove_last(), 11)
        self.assertEqual(dll.__str__(), "[5, 7]")
        self.assertEqual(dll.remove_last(), 7)
        self.assertEqual(dll.remove_last(), 5)
        self.assertIsNone(dll.remove_last())

    def test_length(self):
        """ Tests getting the length of DLL. """
        dll = DoublyLinkedList()
        dll.append(5)

        self.assertEqual(dll.length(), 1)
        dll.append(7)
        self.assertEqual(dll.length(), 2)
        dll.remove_first()
        dll.remove_first()
        self.assertEqual(dll.length(), 0)


if __name__ == "__main__":
    unittest.main()