# Author:  Joshua Fogus
# Course:  CS 325_400_F2020
# Date:  December 02, 2020
# Description:  Implements a FIFO Queue with limited functionality.

from DoublyLinkedList import DoublyLinkedList


class Queue:
    def __init__(self):
        self.__queue = DoublyLinkedList()

    def enqueue(self, val):
        """ Adds a value onto the end of the queue. O(1) """
        self.__queue.append(val)

    def dequeue(self):
        """ Removes and returns a value from the beginning of the stack. O(1) """
        return self.__queue.remove_first()

    def length(self):
        """ Returns the number of elements in the queue. O(n) """
        return self.__queue.length()

    def __str__(self):
        return self.__queue.__str__()


if __name__ == "__main__":
    print("This is not meant to be run as a script. Please import this module.")