"""
Clone of 2048 game.
"""

import random

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}

def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    ls = []
    lenght_of_line = len(line)
    for index in line:
        if index == 0: continue
        ls.append(index)
    razlika = int(lenght_of_line - len(ls))
    nulls = ls
    null  = [0]*razlika
    nulls += null
    for j in range(len(nulls)):
        if j == len(nulls) - 1: continue
        if nulls[j] == nulls[j+1]:
            nulls[j] += nulls[j+1]
            nulls.pop(j + 1)
            nulls.append(0)
    # replace with your code
    return nulls

class TwentyFortyEight():
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        self.grid_width = grid_width
        self.grid_height = grid_height
        self.reset()

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        # replace with your code
        self.grid =  [[0 for row in range(self.grid_width)]for col in range(self.grid_height)]
        col_rand_first = random.randint(0,self.grid_width-1)
        row_rand_first = random.randint(0,self.grid_width-1)
        while True:
            col_rand_sec = random.randint(0,self.grid_width-1)
            row_rand_sec = random.randint(0,self.grid_width-1)
            if col_rand_first != col_rand_sec or row_rand_first!=row_rand_sec:
                break
        prob = random.random()
        if prob >= 0.9:
            self.set_tile(row_rand_first, col_rand_first, 4)
        else:
            self.set_tile(row_rand_first, col_rand_first, 2)
        prob = random.random()
        if prob >= 0.9:
            self.set_tile(row_rand_sec, col_rand_sec, 4)
        else:
            self.set_tile(row_rand_sec, col_rand_sec, 2)

    
    def __str__(self):
        """
        Return a string representation of the grid for debugging
        """
        
        return ' ' + str(self.grid).replace('],', '] \n').replace('[[', '[').replace(']]', ']') 

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        # replace with your code
        return self.grid_height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        # replace with your code
        return self.grid_width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        # replace with your code
        if direction == UP:
            for index_col in range(self.grid_width):
                new_col = merge([col[index_col] for col in self.grid])
                for index_row in range(self.grid_height):
                    self.grid[index_row][index_col] = new_col[index_row]
                    
                    
        if direction == DOWN:
            for index_col in range(self.grid_width):
                col = [col[index_col] for col in self.grid]
                col.reverse()
                new_col = merge(col)
                new_col.reverse()
                for index_list in range(self.grid_height):
                    self.grid[index_list][index_col] = new_col[index_list]
        
        if direction == RIGHT:
            for index_row in range(self.get_grid_height()):
                row = self.grid[index_row]
                row.reverse()
                new_col = merge(row)  
                new_col.reverse()
                self.grid[index_row] = new_col
                    
        if direction == LEFT:
            for index_row in range(self.get_grid_height()):
                new_col = merge(self.grid[index_row])  
                self.grid[index_row] = new_col
        self.new_tile()
        
    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        # replace with your code
        list_of_zero =[]
        for row in range(self.grid_height):
            for col in range(self.grid_width):
                if  self.get_tile(row,col) == 0:
                    list_of_zero.append((row,col))
        if list_of_zero:
            element = random.choice(list_of_zero)
            prob = random.random()
            if prob >= 0.9:
                self.set_tile(element[0], element[1], 4)
            else:
                self.set_tile(element[0], element[1], 2)
        
                

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        # replace with your code
        self.grid[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        # replace with your code
        return self.grid[row][col]


a = TwentyFortyEight(4,5)