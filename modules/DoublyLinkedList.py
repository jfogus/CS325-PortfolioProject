# Author:  Joshua Fogus
# Course:  CS 325_400_F2020
# Date:  December 02, 2020
# Description:  Implements a doubly linked list.


class Node:
    """ A node for a doubly linked list. """
    def __init__(self, val, next_node=None, prev_node=None):
        self.__val = val
        self.__next = next_node
        self.__prev = prev_node

    @property
    def val(self):
        return self.__val

    @val.setter
    def val(self, val):
        self.__val = val

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, next_node):
        self.__next = next_node

    @property
    def prev(self):
        return self.__prev

    @prev.setter
    def prev(self, prev):
        self.__prev = prev


class DoublyLinkedList:
    """ A doubly linked list with insertion and retrieval only from the ends. """
    def __init__(self):
        self.__sentinel = Node(None)
        self.__sentinel.next = self.__sentinel
        self.__sentinel.prev = self.__sentinel

    @property
    def sentinel(self):
        return self.__sentinel

    def append(self, val):
        """ Add a node to the end of the doubly linked list. O(1) """
        new_node = Node(val, self.__sentinel, self.__sentinel.prev)

        self.__sentinel.prev.next = new_node
        self.__sentinel.prev = new_node

    def prepend(self, val):
        """ Add a node to the beginning of the doubly linked list. O(1) """
        new_node = Node(val, self.__sentinel.next, self.__sentinel)

        self.__sentinel.next.prev = new_node
        self.__sentinel.next = new_node

    def remove_first(self):
        """ Removes and returns the value from the first node. """
        val = self.sentinel.next.val
        self.__sentinel.next = self.__sentinel.next.next

        return val

    def remove_last(self):
        """ removes and returns the value from the last node. """
        val = self.__sentinel.prev.val
        self.__sentinel.prev.prev.next = self.__sentinel

        return val

    def __str__(self):
        flat_dll = []
        node = self.__sentinel.next

        # Flatten the DLL
        while node is not self.__sentinel:
            flat_dll.append(node.val)
            node = node.next

        return "{}".format(flat_dll)


if __name__ == "__main__":
    print("This is not meant to be run as a script. Please import this module.")