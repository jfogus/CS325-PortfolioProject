# Author:  Joshua Fogus
# Course:  CS 325_400_F2020
# Date:  December 06, 2020
# Description:  Implements a Corral game for user input to update.

from Certificate import Certificate


class Game:
    """ Receives a tuple of dimensions, with the 0th item being the rows and the 1st
        item being the columns, and a dictionary of conditions in the form of
        { x, y: integer }. """
    def __init__(self, dimensions, conditions):
        self.__board = [[[] for _ in range(dimensions[1])] for _ in range(dimensions[0])]
        self.__certificate = Certificate(conditions)

    @property
    def board(self):
        return self.__board

    def print_board(self):
        """ Pretty prints the board. """
        for row in self.__board:
            for col in row:
                print(col, end=" ")
            print()


if __name__ == "__main__":
    g = Game((7, 7), {
        (1, 0): 3,
        (2, 1): 4,
        (1, 3): 2
    })
    g.print_board()
    print("This is not meant to be run as a script. Please import this module.")
