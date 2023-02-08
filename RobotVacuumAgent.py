import random

"""I have improved the robot to make it act in a rational way.
Before modifications, this code used the random library to instruct
the robot to move about the room. This was inefficient, taking
hundreds of moves for the robot to complete the task. I modified the 
code by using a dictionary of dirty spaces so that the robot can keep 
track of the closest space and moves towards the closest one. This is 
rational behavior because it acts in a way that will minimize steps needed
to clean the room instead of acting randomly."""



class RobotVacuumAgent:

    def __init__(self,filename):
        """
        init function establishes board, robotRow, robotCol
        :param filename: establishes board
        """
        with open(filename, "r") as file:
            self.board = [[x for x in line.split()] for line in file]

        self.num_spaces   = 0  # number of potential clean/dirty spaces in board
        
        # idea/suggestion: define variables to keep track of the dirty locations
        # introduce a dictionary to store dirty locations with its distance from the robot's current position
        #      eg, 'key' in this dictionary could be (r,c) and 'value' could be distance                
        self.dirty_spaces = {} # dictionary of dirty spaces with distance
        self.closest_dirt = 0  # for keeping track of the closest dirt location
        
        for r in range(len(self.board)):
            for c in range(len(self.board[r])):
                self.num_spaces += 1
                if self.board[r][c] == '@' or self.board[r][c] == '!': # find the location of the robot
                    self.robotRow = r;
                    self.robotCol = c;
                    
        
        # idea/suggestion: save the locations (row_number: 'r' and column_number: 'c') of the dirty places
        #                  you could save it in self.dirty_spaces
        #    for r in range(len(self.board)):
        #        for c in range(len(self.board[r])):
        #            if self.board[r][c] == '*':
        
        # idea/suggestion: compute the closest location and save it to self.closest_dirt

        #Compute the distance values as suggested above and store them in a dictionary
        for r in range(len(self.board)):
            for c in range(len(self.board[r])):
                if self.board[r][c] == '*':
                    distance_to_dirt = (abs(0 - r) + abs(0 - c))
                    self.dirty_spaces[(r,c)] = distance_to_dirt
        
        #Determine the closest dirt and store that ordered pair in the self.closest_dirt variable
        for key in self.dirty_spaces:
            if self.dirty_spaces[key] == min(self.dirty_spaces.values()):
                self.closest_dirt = key
                break
            else:
                pass
        

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
        print("Doing something")
        if self.board[self.robotRow][self.robotCol] == '!':
            self.board[self.robotRow][self.robotCol] = '@'; #just sucked up the dirt
            if len (self.dirty_spaces) > 0:
                self.dirty_spaces.pop(self.closest_dirt)
                #Recalculate the distances after sucking up the dirt
                self.compute_distances()
        else:
            # TBD: you can comment out the above portion of the code and replace it with 
            # a more intelligent strategy to pick the next location where the robot could move.
            # For example, it could be based on the self.closest_dirt

            #Determine the next movement based on the position of the next closest dirt
            #Move one unit toward the dirt in whatever direction is necessary
            if self.robotRow < self.closest_dirt[0]:
                self.move_down()
            elif self.robotRow > self.closest_dirt[0]: 
                self.move_up()
            elif self.robotCol < self.closest_dirt[1]:
                self.move_right()
            elif self.robotCol > self.closest_dirt[1]:
                self.move_left()
    
    #This is a helper function used to evaluate the position of the dirt relative to the robot
    #After every movement, this function is called to determine the next closest dirt
    def compute_distances(self):
        #Iterate over the keys in the dirty spaces dictionary
        for key in self.dirty_spaces:   
            #Recalculate the distance to the next closest dirt based on the current position
            #of the robot         
            distance_to_dirt = (abs(self.robotRow - key[0]) + abs(self.robotCol - key[1]))
            self.dirty_spaces[key] = distance_to_dirt
        #Iterate over the keys in the dictionary after calculating the distances to check
        #What the next closest dirt is. 
        for key in self.dirty_spaces:
            if self.dirty_spaces[key] == min(self.dirty_spaces.values()):
                self.closest_dirt = key
                break
            else:
                pass


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
            
            #Recalculate distances after movement
            self.compute_distances()
                

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
            
            #Recalculate distances after movement
            self.compute_distances()


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

            #Recalculate distances after movement
            self.compute_distances()

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

            #Recalculate distances after movement
            self.compute_distances()



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
    agent = RobotVacuumAgent("room3.txt")

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