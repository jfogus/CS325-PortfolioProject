# Author:  Joshua Fogus
# Course:  CS 325_400_F2020
# Date:  December 03, 2020
# Description:  Implements an edge object. All operations in O(1).


class Edge:
    def __init__(self, u, v):
        self.__u = u
        self.__v = v

    @property
    def u(self):
        return self.__u

    @property
    def v(self):
        return self.__v

    def is_valid_length(self, req_length):
        """ Receives a required length as an integer >= 2, returns True
            if the length of the edge is equal to the required length.
            Otherwise, returns false. O(1) """
        if self.get_length() == req_length and req_length >= 2:
            return True

        return False

    def get_length(self):
        """ Returns Manhattan distance between vertices. O(1) """
        return abs(self.__u.y - self.__v.y) + abs(self.__u.x - self.__v.x)

    def is_aligned(self):
        """ Aligned means both vertices are in the same column or row. O(1) """
        if self.__u.x == self.__v.x or self.__u.y == self.__v.y:
            return True

        return False

    def get_slope(self):
        """ Gets the slope of the edge. O(1) """
        # Vertical line
        if self.__u.x == self.__v.x:
            return None

        return (self.__u.y - self.__v.y) / (self.__u.x - self.__v.x)

    def is_intersected_by(self, vertex):
        """ Returns true if the given vertex is between the two points
            of the edge. O(1) """
        edge1 = Edge(self.__u, vertex)
        edge2 = Edge(vertex, self.__v)

        if edge1.get_length() == 0 or \
                edge2.get_length() == 0 or \
                (edge1.get_slope() == edge2.get_slope() and
                 edge1.get_length() <= self.get_length() and
                 edge2.get_length() <= self.get_length()):
            return True

        return False


if __name__ == "__main__":
    print("This is not meant to be run as a script. Please import this module.")