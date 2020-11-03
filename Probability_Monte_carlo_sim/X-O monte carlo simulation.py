# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 18:50:27 2020

@author: Freedom
"""

"""
Monte Carlo Tic-Tac-Toe Player
"""

import random


# Constants for Monte Carlo simulator
# You may change the values of these constants as desired, but
#  do not change their names.
PLAYERX = 1
PLAYERO = 2
EMPTY = 0
DRAW = 3

NTRIALS = 100         # Number of trials to run
SCORE_CURRENT = 1.0 # Score for squares played by the current player
SCORE_OTHER = 1.0   # Score for squares played by the other player
    
# Add your functions here.
class TTTBoard():
    """
    Class to represent a Tic-Tac-Toe board.
    """

    def __init__(self, dim, reverse = False, board = None):
        """
        Initialize the TTTBoard object with the given dimension and 
        whether or not the game should be reversed.
        """
        self.dim = dim
        self.int_board = [[0 for col in range(self.dim)] for row in range(self.dim)]
        self.score = [[0 for col in range(self.dim)] for row in range(self.dim)]
        
    def __str__(self):
        """
        Human readable representation of the board.
        """
        return ' ' + str(self.int_board).replace('],', '] \n').replace('[[', '[').replace(']]', ']')
    def get_dim(self):
        """
        Return the dimension of the board.
        """
        return self.dim
    
    def square(self, row, col):
        """
        Returns one of the three constants EMPTY, PLAYERX, or PLAYERO 
        that correspond to the contents of the board at position (row, col).
        """
        # if self.int_board[row][col] == EMPTY:
        #     return EMPTY
        # elif self.int_board[row][col] == PLAYERX:
        #     return PLAYERX
        # else:
        #     return PLAYERO
        return self.int_board[row][col]
        #DRAW
    def get_empty_squares(self):
        """
        Return a list of (row, col) tuples for all empty squares
        """
        list_of_zeroes = []
        for row in range(self.get_dim()):
            for col in range(self.get_dim()):
                if self.int_board[row][col] == 0:
                    list_of_zeroes.append((row,col))
        return list_of_zeroes
    def move(self, row, col, player):
        """
        Place player on the board at position (row, col).
        player should be either the constant PLAYERX or PLAYERO.
        Does nothing if board square is not empty.
        """
        self.int_board[row][col] = player

    def check_win(self):
        """
        Returns a constant associated with the state of the game
            If PLAYERX wins, returns PLAYERX.
            If PLAYERO wins, returns PLAYERO.
            If game is drawn, returns DRAW.
            If game is in progress, returns None.
        """
        for row_index in range(self.dim):
            if len(set(self.int_board[row_index])) == 1 and self.int_board[row_index][0] != 0 :
                return self.square(row_index,0)
        for index_col in range(self.dim):
                col = [col[index_col] for col in self.int_board]
                if len(set(col)) == 1 and col[0] != 0:
                    return self.square(0,index_col)
        diag = [ self.int_board[i][i] for i in range(self.dim) ]
        if len(set(diag)) == 1 and self.int_board[0][0] != 0:
            return self.square(0,0)
        diag_rev = [ self.int_board[-(i+1)][i] for i in range(self.dim) ]
        if len(set(diag_rev)) == 1 and self.int_board[-1][0] != 0:
            return self.square(0,0)
        if len(self.get_empty_squares())== 0 :
            return DRAW
        return None
    def clone(self):
        """
        Return a copy of the board.
        """
        return self.int_board.copy()
board = TTTBoard(3)

def mc_trial(board, player ): 
        copy_of_player = player #made a copy of player
        while board.check_win() is None:
            empty = random.choice(board.get_empty_squares())
            board.move(empty[0], empty[1], copy_of_player)
            if copy_of_player == PLAYERX:
                copy_of_player = PLAYERO
            elif copy_of_player == PLAYERO:
                copy_of_player = PLAYERX
# mc_trial(board, PLAYERX)
# print(board)             
def mc_update_scores (scores, board, player):
    who_won = board.check_win()
    SCORE_CURRENT_ = SCORE_CURRENT
    SCORE_OTHER_ = SCORE_OTHER
    if who_won == player:
        SCORE_OTHER_ = SCORE_OTHER_ * -1
    elif who_won == DRAW:
        return
    else:
        SCORE_CURRENT_ = SCORE_CURRENT_ * -1
    for row in range(board.dim):
        for col in range(board.dim):
            if board.square(row,col) == player:
                scores[row][col] += SCORE_CURRENT_
            elif board.square(row,col) == EMPTY:
                continue
            else:
                scores[row][col] += SCORE_OTHER_

# mc_trial(board, PLAYERX)
# print(board)
# mc_update_scores(board.score, board, PLAYERX )
# print(board.score)
def get_best_move(board, scores):
    tuples = board.get_empty_squares()
    best = tuples[0]
    best_score = board.score[best[0]][best[1]]
    for iteration in tuples:
        if board.score[iteration[0]][iteration[1]] > best_score:
            best_score = board.score[iteration[0]][iteration[1]]
            best = iteration

def mc_move(board, player, trials):
    for trail in range(trials):
        mc_trial(board, PLAYERX)
        mc_update_scores(board.score, board, PLAYERX )
    return get_best_move(board, board.score)

mc_move(board, 1, 10)
    
    
            
                
    
    
        

        


# Test game with the console or the GUI.  Uncomment whichever 
# you prefer.  Both should be commented out when you submit 
# for testing to save time.

# play_game(mc_move, NTRIALS, False)        
# poc_ttt_gui.run_gui(3, PLAYERX, mc_move, NTRIALS,

# import random
# br_simulacija = 1001
# a=0
# b=0
# for i in range(br_simulacija):
#     a_random = random.random()
#     if a_random > 0.49999:
#         a+=1
#     else:
#         b+=1    
# if a > b:
#     print('Jebiga brate, to je to')
# else:
#     print("IDEMO DALJE! NEMA PREDAJE")