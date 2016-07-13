import homework4 as hw4
import unittest
import timeit

class TestSudoku(unittest.TestCase):
    def test_read_board(self):
        d = hw4.read_board("sudoku/medium1.txt");
        s = hw4.Sudoku(d);
        self.assertEquals(s.get_values((0,0)),\
            set([1, 2, 3, 4, 5, 6, 7, 8, 9]));
        self.assertEquals(s.get_values((0, 1)), set([1]));

    def test_sudoku_cells(self):
        
        self.assertEquals(len(hw4.sudoku_cells()) , 81);

    def test_sudoku_arcs(self):
        self.assertTrue(((0, 0), (0, 8)) in hw4.sudoku_arcs());
        self.assertTrue(((0, 0), (8, 0)) in hw4.sudoku_arcs());
        self.assertTrue(((0, 8), (0, 0)) in hw4.sudoku_arcs());
        self.assertTrue(((0, 0), (2, 1)) in hw4.sudoku_arcs());
        self.assertTrue(((2, 2), (0, 0)) in hw4.sudoku_arcs());
        self.assertFalse(((2, 3), (0, 0)) in hw4.sudoku_arcs());
        self.assertFalse(((3, 1), (0, 0)) in hw4.sudoku_arcs());

    def test_remove_inconsistent_values(self):
        sudoku = hw4.Sudoku(hw4.read_board("sudoku/easy.txt"));
        self.assertEquals(sudoku.get_values((0, 3)), set([1, 2, 3, 4, 5, 6, 7, 8, 9]));
        self.assertTrue(sudoku.remove_inconsistent_values((0, 3), (0, 0)));
        self.assertTrue(sudoku.remove_inconsistent_values((0, 3), (0, 1)));
        self.assertFalse(sudoku.remove_inconsistent_values((0, 3), (0, 4)));

    def print_sudoku(self,sudoku):
        s = [[0]*9 for i in xrange(9)]
        for r, c in sudoku.board:
            s[r][c] = sudoku.board[(r,c)]
        for row in s:
            print row

    def test_infer_ac3(self):
        sudoku = hw4.Sudoku(hw4.read_board("sudoku/medium2.txt"));
        #self.print_sudoku(sudoku)
        sudoku.infer_ac3();
        #self.print_sudoku(sudoku)

    def test_infer_improves(self):
        sudoku = hw4.Sudoku(hw4.read_board("sudoku/medium4.txt"));
        sudoku.infer_improved();
        self.print_sudoku(sudoku)

    def test_infer_with_guessing(self):
        sudoku = hw4.Sudoku(hw4.read_board("sudoku/hard3.txt"));
        sudoku.infer_with_guessing();
        self.print_sudoku(sudoku);

    
        
        

        
if __name__ == '__main__':
    unittest.main()

