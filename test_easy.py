import homework4 as hw4
import unittest
import timeit

class TestSudoku(unittest.TestCase):
    def print_sudoku(self,sudoku):
        s = [[0]*9 for i in xrange(9)]
        for r, c in sudoku.board:
            s[r][c] = sudoku.board[(r,c)]
        for row in s:
            print row

    def test_infer_ac3(self):
        sudoku = hw4.Sudoku(hw4.read_board("sudoku/easy.txt"));
        sudoku.infer_ac3();
        self.print_sudoku(sudoku)

        

        
if __name__ == '__main__':
    unittest.main()

