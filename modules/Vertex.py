# Author:  Joshua Fogus
# Course:  CS 325_400_F2020
# Date:  December 02, 2020
# Description:  Implments a vertex for use in a graph.


class Vertex:
    """ Implementation of a vertex with x and y coordinates. """
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        """ Getter for the x coordinate. """
        return self.__x

    @property
    def y(self):
        """ Getter for the y coordinate. """
        return self.__y

    @property
    def coords(self):
        """ Returns a tuple of the coordinates. """
        return self.__x, self.__y


if __name__ == "__main__":
    print("This is not meant to be run as a script. Please import this module.")
