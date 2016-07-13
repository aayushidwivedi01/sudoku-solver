############################################################
# CIS 521: Homework 4
############################################################

student_name = "Aayushi Dwivedi"

############################################################
# Imports
############################################################

# Include your imports here, if any are used.
from collections import deque
from copy import deepcopy
import random
############################################################
# Section 1: Sudoku
############################################################

def sudoku_cells():
    return set([ (row, col) for col in xrange(9) for row in xrange(9)]);

def sudoku_arcs():
    return [((row, col), (n_row, n_col)) for (n_row, n_col) in sudoku_cells() for (row, col) in sudoku_cells()\
          if (row, col) != (n_row, n_col) and (row == n_row or col == n_col or\
         (row/3 == n_row/3 and col/3 == n_col /3))]
            
def sudoku_neighbors(arcs):
    d = dict();
    for (cell1, cell2) in arcs:
        if cell1 in d:
            d[cell1] += [(cell2, cell1)];
        else:
            d[cell1] = [(cell2, cell1)];
    return d;   
def read_board(path):
    fopen = open(path, 'r');
    row = 0;
    col = 0;
    board = dict();
    while True:
        val = fopen.read(1);
        if not val:
            break;
        if val.isdigit():
            board[(row, col)] = set([int(val)])
            col +=1
        elif val == "*":
            board[(row, col)] =  set([1,2,3,4,5,6,7,8,9]);
            col += 1;
        if col >= 9:
            row += 1;
            col = 0
    fopen.close();
    return board;

class Sudoku(object):

    CELLS = sudoku_cells()
    ARCS = sudoku_arcs()
    NEIGHBORS = sudoku_neighbors(ARCS);
    def __init__(self, board):
        self.board = board;

    def get_values(self, cell):
        return self.board[cell];

    def remove_inconsistent_values(self, cell1, cell2):
        cell2_set = self.get_values(cell2);
        if len(cell2_set) == 1 and len(self.get_values(cell1)) > 1 and cell2_set.intersection(self.get_values(cell1)):
            self.get_values(cell1).difference_update(cell2_set);
            return True;
        else:
            return False;
        
    def get_neighbors(self, cell):
        return Sudoku.NEIGHBORS[cell];

    def infer_ac3(self):
        queue = set(Sudoku.ARCS);
        while len(queue) > 0:
            (cell1, cell2) = queue.pop();
            if self.remove_inconsistent_values(cell1, cell2):
                neighbors = set(self.get_neighbors(cell1));
                neighbors.remove((cell2, cell1));
                queue.update(neighbors);
    
    def infer_improved(self):
        done = False;
        
        while not done:
            self.infer_ac3();
            for (cell, values) in self.board.iteritems():
                if len(values) > 1:
                    neighbor = self.get_neighbors(cell);

                    neighbors_col = {val for s in [self.board[(i, cell[1])] for i in xrange(9) \
                                        if (i, cell[1]) <> cell] for val in s}
                    neighbors_row = {val for s in [self.board[(cell[0], i)] for i in xrange(9) \
                                        if (cell[0], i) <> cell] for val in s}
                    neighbors_block = {val for s in [self.board[(i,j)] for j in xrange(9) for i in xrange(9)\
                                        if (i, j) <> cell and (i/3 == cell[0]/3) and (j/3 == cell[1]/3)\
                                        ] for val in s}
                    found = True;
                    for value in values:
                        if value not in neighbors_col or value not in neighbors_row or value not in neighbors_block:
                            self.board[cell] = set([value]);
                            found = False;
                            done = False;
                            break;
                    if not found:
                        break;
                else:
                    done = True; 

    def is_solved(self):
        for (cell1, cell2) in Sudoku.ARCS:
            c1 = self.board[cell1]
            c2 = self.board[cell2]
            if len(c1)<> 1 or len(c2)<>1 or (len(c1) == 1 and len(c2) == 1\
            and c1.intersection(c2)):
                return False;
        return True
            

    def infer_with_guessing(self):
        if self.is_solved():
            return;

        self.infer_improved();
        for cell, values in self.board.iteritems():
            if len(values) > 1:
                for value in values:
                    #value = random.sample(values, 1);
                    new_game = Sudoku(deepcopy(self.board))
                    new_game.board[cell] = set([value]);
                    new_game.infer_with_guessing();
                    if new_game.is_solved():
                        self.board = new_game.board;
                        return;
                    #values.remove(value[0])
                return;
                           

############################################################
# Section 2: Feedback
############################################################

feedback_question_1 = """
~10hrs
"""

feedback_question_2 = """
It was fairly easy but I took some time with
infer_with_guessing.
"""

feedback_question_3 = """
I like how small changes in algorithm improved the
results. I wouldn't change anything about the assignment.
"""
