# Author:  Joshua Fogus
# Course:  CS 325_400_F2020
# Date:  December 02, 2020
# Description:  Implements a doubly linked list.


class Node:
    """ A node for a doubly linked list. """
    def __init__(self, val, nextNode=None, prevNode=None):
        self.__val = val
        self.__next = nextNode
        self.__prev = prevNode

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
    def next(self, next):
        self.__next = next

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

    @property
    def head(self):
        return self.__sentinel

    def append(self, val):
        """ Add a node to the end of the doubly linked list. O(1) """
        self.__sentinel.prev = Node(val, self.__sentinel, self.__sentinel.prev)

    def prepend(self, val):
        """ Add a node to the beginning of the doubly linked list. O(1) """
        self.__sentinel.next = Node(val, self.__sentinel.next, self.__sentinel)


if __name__ == "__main__":
    print("This is not meant to be run as a script. Please import this module.")