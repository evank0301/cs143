import random

class RobotVacuumAgent:

    def __init__(self,filename):
        """
        init function establishes board, robotRow, robotCol
        :param filename: establishes board
        """
        with open(filename, "r") as file:
            self.board = [[x for x in line.split()] for line in file]

        self.num_spaces = 0 # number of potential clean/dirty spaces in board

        for r in range(len(self.board)):
            for c in range(len(self.board[r])):
                self.num_spaces += 1
                if self.board[r][c] == '@' or self.board[r][c] == '!': # find the location of the robot
                    self.robotRow = r;
                    self.robotCol = c;


    def print(self):
        """
        displays board to console
        """
        for r in range(len(self.board)):
            for c in range(len(self.board[r])):
                print(self.board[r][c], end = ' ')
            print()


    def do_something(self):
        """
        can do two actions: either "suck up dirt" or "move in either of the four directions"
        """
        if self.board[self.robotRow][self.robotCol] == '!':
            self.board[self.robotRow][self.robotCol] = '@'; #just sucked up the dirt
        else:
            rand = random.randint(0,3)
            if rand == 0:
                self.move_up()
            elif rand == 1:
                self.move_down()
            elif rand == 2:
                self.move_left()
            else:
                self.move_right()

    def out_of_bounds(self, row, col):
        """
        :param row:
        :param col:
        :return: True if (row,col) will be out of bounds of self.board
                otherwise, returns False
        """
        try:
            if row < 0 or row >= len(self.board) or col < 0 or col >= len(self.board[row]):
                return True
            else:
                return False
        except:
            print('exception occurred -- out of bounds')
            return True


    def move_up(self):
        """
        moves robot 1 space up (north)
        :return:
        """
        if not self.out_of_bounds(self.robotRow -1, self.robotCol):
            if self.board[self.robotRow][self.robotCol] == '@':
                self.board[self.robotRow][self.robotCol] = '.'
            elif self.board[self.robotRow][self.robotCol] == '!':
                self.board[self.robotRow][self.robotCol] = '*'
            self.robotRow -= 1
            if self.board[self.robotRow][self.robotCol] == '*':
                self.board[self.robotRow][self.robotCol] = '!'
            elif self.board[self.robotRow][self.robotCol] == '.':
                self.board[self.robotRow][self.robotCol] = '@'

    def move_down(self):
        """
        moves robot 1 space down (south)
        :return:
        """
        if not self.out_of_bounds(self.robotRow+1, self.robotCol):
            if self.board[self.robotRow][self.robotCol] == '@':
                self.board[self.robotRow][self.robotCol] = '.'
            elif self.board[self.robotRow][self.robotCol] == '!':
                self.board[self.robotRow][self.robotCol] = '*'
            self.robotRow += 1
            if self.board[self.robotRow][self.robotCol] == '*':
                self.board[self.robotRow][self.robotCol] = '!'
            elif self.board[self.robotRow][self.robotCol] == '.':
                self.board[self.robotRow][self.robotCol] = '@'


    def move_left(self):
        """
        moves robot 1 space left (west)
        :return:
        """
        if not self.out_of_bounds(self.robotRow, self.robotCol-1):
            if self.board[self.robotRow][self.robotCol] == '@':
                self.board[self.robotRow][self.robotCol] = '.'
            elif self.board[self.robotRow][self.robotCol] == '!':
                self.board[self.robotRow][self.robotCol] = '*'
            self.robotCol -= 1
            if self.board[self.robotRow][self.robotCol] == '*':
                self.board[self.robotRow][self.robotCol] = '!'
            elif self.board[self.robotRow][self.robotCol] == '.':
                self.board[self.robotRow][self.robotCol] = '@'


    def move_right(self):
        """
         moves robot 1 space right (east)
         :return:
         """
        if not self.out_of_bounds(self.robotRow, self.robotCol+1):
            if self.board[self.robotRow][self.robotCol] == '@':
                self.board[self.robotRow][self.robotCol] = '.'
            elif self.board[self.robotRow][self.robotCol] == '!':
                self.board[self.robotRow][self.robotCol] = '*'
            self.robotCol += 1
            if self.board[self.robotRow][self.robotCol] == '*':
                self.board[self.robotRow][self.robotCol] = '!'
            elif self.board[self.robotRow][self.robotCol] == '.':
                self.board[self.robotRow][self.robotCol] = '@'


    def utility(self):
        """
        :return: the number of clean spots in the room
        """
        result = 0
        for r in range(len(self.board)):
            for c in range(len(self.board[r])):
                if self.board[r][c] == '.' or self.board[r][c] == '@':
                    result += 1
        return result

    def is_goal(self):
        """
        :return: True if all of the spaces are clean; otherwise, False
        """
        if self.utility() == self.num_spaces:
            return True
        else:
            return False


if __name__ == '__main__':
    # create agent
    agent = RobotVacuumAgent("room1.txt")

    count = 0; # number of time steps

    # run the vacuum until room is clean
    while not agent.is_goal():
        print("Number of moves: ", count)
        agent.print()

        count += 1
        agent.do_something()

    # final state
    print("Completed the task with ", count, " moves.")
    agent.print()