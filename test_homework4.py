import unittest
import homework4 as hw4

class TestSudoku(unittest.TestCase):
	
	def test_read_board(self):
		b = hw4.read_board("sudoku/easy.txt")
		s = hw4.Sudoku(b)
		self.assertEqual(s.get_values((0,0)), set([8]))
		self.assertEqual(s.get_values((3,2)), set([8]))
		self.assertEqual(s.get_values((4,8)), set([4]))
		self.assertEqual(s.get_values((5,2)), set([1,2,3,4,5,6,7,8,9]))
		self.assertEqual(s.get_values((6,6)), set([1]))
		self.assertEqual(s.get_values((7,1)), set([7]))
		self.assertEqual(s.get_values((7,0)), set([1,2,3,4,5,6,7,8,9]))
		self.assertEqual(s.get_values((7,2)), set([1,2,3,4,5,6,7,8,9]))
		self.assertEqual(s.get_values((8,0)), set([9]))
		self.assertEqual(s.get_values((8,2)), set([2]))
		self.assertEqual(s.get_values((8,4)), set([1,2,3,4,5,6,7,8,9]))
		self.assertEqual(s.get_values((8,8)), set([6]))
		b = hw4.read_board("sudoku/medium1.txt")
		s = hw4.Sudoku(b)
		self.assertEqual(s.get_values((0,0)), set([1,2,3,4,5,6,7,8,9]))
		self.assertEqual(s.get_values((0,1)), set([1]))
		
		
	def test_sudoku_arcs(self):
		arcs = hw4.Sudoku.ARCS
		self.assertTrue(((0, 0), (0, 8)) in arcs)
		self.assertTrue(((0, 0), (8, 0)) in arcs)
		self.assertTrue(((0, 8), (0, 0)) in arcs)
		self.assertTrue(((0, 0), (2, 1)) in arcs)
		self.assertTrue(((0, 0), (2, 2)) in arcs)
		self.assertTrue(((0, 3), (0, 5)) in arcs)
		self.assertTrue(((0, 3), (2, 5)) in arcs)
		self.assertTrue(((0, 3), (2, 3)) in arcs)
		self.assertFalse(((0, 2), (1, 3)) in arcs)
		self.assertFalse(((0, 0), (2, 3)) in arcs)
		self.assertFalse(((0, 0), (3, 3)) in arcs)
		self.assertFalse(((0, 0), (4, 4)) in arcs)
		self.assertFalse(((0, 0), (5, 5)) in arcs)
		self.assertFalse(((0, 0), (6, 6)) in arcs)
		self.assertFalse(((0, 0), (7, 7)) in arcs)
	
	def test_remove_inconsistent_values(self):
		sudoku = hw4.Sudoku(hw4.read_board("sudoku/easy.txt")) 
		self.assertEqual(sudoku.get_values((0, 3)), set([1,2,3,4,5,6,7,8,9]))
		self.assertTrue(sudoku.remove_inconsistent_values((0, 3), (0, 0)))
		self.assertTrue(sudoku.remove_inconsistent_values((0, 3), (0, 1)))
		self.assertFalse(sudoku.remove_inconsistent_values((0, 3), (0, 4)))
		
	# def test_infer_ac3(self):
		# sudoku = hw4.Sudoku(hw4.read_board("sudoku/easy.txt")) 
		# sudoku.infer_ac3()
		# self.assertEqual(sudoku.board, {(7, 3): set([1]), (4, 7): set([8]), (1, 3): set([8]), (4, 8): set([4]), (3, 0): set([7]), (2, 8): set([5]), (8, 0): set([9]), (7, 8): set([8]), (5, 4): set([8]), (0, 7): set([9]), (5, 6): set([7]), (2, 6): set([8]), (1, 6): set([4]), (5, 1): set([4]), (3, 7): set([3]), (0, 3): set([5]), (8, 5): set([8]), (2, 5): set([2]), (5, 8): set([1]), (4, 0): set([1]), (1, 2): set([3]), (7, 4): set([5]), (6, 4): set([2]), (3, 3): set([2]), (2, 0): set([4]), (8, 1): set([1]), (7, 6): set([9]), (4, 4): set([9]), (6, 3): set([4]), (1, 5): set([7]), (8, 8): set([6]), (7, 2): set([4]), (3, 6): set([6]), (2, 2): set([7]), (7, 7): set([2]), (5, 7): set([5]), (5, 3): set([6]), (4, 1): set([3]), (1, 1): set([9]), (2, 7): set([1]), (3, 2): set([8]), (0, 0): set([8]), (6, 6): set([1]), (5, 0): set([2]), (7, 1): set([7]), (4, 5): set([5]), (0, 4): set([6]), (5, 5): set([3]), (1, 4): set([1]), (6, 0): set([6]), (7, 5): set([6]), (2, 3): set([9]), (2, 1): set([6]), (8, 7): set([4]), (6, 8): set([3]), (4, 2): set([6]), (1, 0): set([5]), (0, 8): set([7]), (6, 5): set([9]), (3, 5): set([1]), (0, 1): set([2]), (8, 3): set([3]), (7, 0): set([3]), (4, 6): set([2]), (6, 7): set([7]), (8, 6): set([5]), (5, 2): set([9]), (6, 1): set([8]), (3, 1): set([5]), (8, 2): set([2]), (2, 4): set([3]), (3, 8): set([9]), (0, 6): set([3]), (1, 8): set([2]), (6, 2): set([5]), (4, 3): set([7]), (1, 7): set([6]), (0, 5): set([4]), (3, 4): set([4]), (0, 2): set([1]), (8, 4): set([7])})
		
	# def test_infer_imporoved(self):
		# sudoku = hw4.Sudoku(hw4.read_board("sudoku/medium1.txt")) 
		# sudoku.infer_improved()
		# self.assertEqual(sudoku.board, {(7, 3): set([7]), (4, 7): set([9]), (1, 3): set([5]), (4, 8): set([6]), (3, 0): set([9]), (2, 8): set([1]), (8, 0): set([2]), (7, 8): set([3]), (5, 4): set([7]), (0, 7): set([4]), (5, 6): set([3]), (2, 6): set([5]), (1, 6): set([7]), (5, 1): set([8]), (3, 7): set([7]), (0, 3): set([3]), (8, 5): set([4]), (2, 5): set([8]), (5, 8): set([5]), (4, 0): set([7]), (1, 2): set([9]), (7, 4): set([9]), (6, 4): set([8]), (3, 3): set([4]), (2, 0): set([3]), (8, 1): set([9]), (7, 6): set([1]), (4, 4): set([5]), (6, 3): set([6]), (1, 5): set([6]), (8, 8): set([7]), (7, 2): set([4]), (3, 6): set([2]), (2, 2): set([7]), (7, 7): set([8]), (5, 7): set([1]), (5, 3): set([2]), (4, 1): set([3]), (1, 1): set([4]), (2, 7): set([6]), (3, 2): set([1]), (0, 0): set([6]), (6, 6): set([9]), (5, 0): set([4]), (7, 1): set([6]), (4, 5): set([1]), (0, 4): set([2]), (5, 5): set([9]), (1, 4): set([1]), (6, 0): set([1]), (7, 5): set([2]), (2, 3): set([9]), (2, 1): set([2]), (8, 7): set([5]), (6, 8): set([4]), (4, 2): set([2]), (1, 0): set([8]), (0, 8): set([9]), (6, 5): set([5]), (3, 5): set([3]), (0, 1): set([1]), (8, 3): set([1]), (7, 0): set([5]), (4, 6): set([4]), (6, 7): set([2]), (8, 6): set([6]), (5, 2): set([6]), (6, 1): set([7]), (3, 1): set([5]), (8, 2): set([8]), (2, 4): set([4]), (3, 8): set([8]), (0, 6): set([8]), (1, 8): set([2]), (6, 2): set([3]), (4, 3): set([8]), (1, 7): set([3]), (0, 5): set([7]), (3, 4): set([6]), (0, 2): set([5]), (8, 4): set([3])})
		
		# sudoku = hw4.Sudoku(hw4.read_board("sudoku/medium2.txt")) 
		# sudoku.infer_improved()
		# self.assertEqual(sudoku.board, {(7, 3): set([3]), (4, 7): set([6]), (1, 3): set([7]), (4, 8): set([4]), (3, 0): set([2]), (2, 8): set([6]), (8, 0): set([6]), (7, 8): set([9]), (5, 4): set([3]), (0, 7): set([7]), (5, 6): set([1]), (2, 6): set([9]), (1, 6): set([8]), (5, 1): set([6]), (3, 7): set([8]), (0, 3): set([6]), (8, 5): set([5]), (2, 5): set([2]), (5, 8): set([2]), (4, 0): set([5]), (1, 2): set([6]), (7, 4): set([7]), (6, 4): set([1]), (3, 3): set([4]), (2, 0): set([7]), (8, 1): set([9]), (7, 6): set([6]), (4, 4): set([2]), (6, 3): set([9]), (1, 5): set([4]), (8, 8): set([8]), (7, 2): set([5]), (3, 6): set([5]), (2, 2): set([4]), (7, 7): set([4]), (5, 7): set([9]), (5, 3): set([5]), (4, 1): set([3]), (1, 1): set([5]), (2, 7): set([3]), (3, 2): set([9]), (0, 0): set([9]), (6, 6): set([2]), (5, 0): set([4]), (7, 1): set([2]), (4, 5): set([9]), (0, 4): set([8]), (5, 5): set([7]), (1, 4): set([9]), (6, 0): set([8]), (7, 5): set([8]), (2, 3): set([1]), (2, 1): set([8]), (8, 7): set([1]), (6, 8): set([7]), (4, 2): set([1]), (1, 0): set([3]), (0, 8): set([5]), (6, 5): set([6]), (3, 5): set([1]), (0, 1): set([1]), (8, 3): set([2]), (7, 0): set([1]), (4, 6): set([7]), (6, 7): set([5]), (8, 6): set([3]), (5, 2): set([8]), (6, 1): set([4]), (3, 1): set([7]), (8, 2): set([7]), (2, 4): set([5]), (3, 8): set([3]), (0, 6): set([4]), (1, 8): set([1]), (6, 2): set([3]), (4, 3): set([8]), (1, 7): set([2]), (0, 5): set([3]), (3, 4): set([6]), (0, 2): set([2]), (8, 4): set([4])})
		
		
		# sudoku = hw4.Sudoku(hw4.read_board("sudoku/medium4.txt")) 
		# sudoku.infer_improved()
		# self.assertEqual(sudoku.board, {(7, 3): set([8]), (4, 7): set([8]), (1, 3): set([6]), (4, 8): set([3]), (3, 0): set([9]), (2, 8): set([2]), (8, 0): set([3]), (7, 8): set([4]), (5, 4): set([4]), (0, 7): set([5]), (5, 6): set([7]), (2, 6): set([6]), (1, 6): set([9]), (5, 1): set([8]), (3, 7): set([4]), (0, 3): set([2]), (8, 5): set([6]), (2, 5): set([4]), (5, 8): set([5]), (4, 0): set([2]), (1, 2): set([2]), (7, 4): set([2]), (6, 4): set([1]), (3, 3): set([5]), (2, 0): set([5]), (8, 1): set([2]), (7, 6): set([3]), (4, 4): set([6]), (6, 3): set([3]), (1, 5): set([3]), (8, 8): set([9]), (7, 2): set([5]), (3, 6): set([2]), (2, 2): set([1]), (7, 7): set([6]), (5, 7): set([9]), (5, 3): set([1]), (4, 1): set([5]), (1, 1): set([4]), (2, 7): set([3]), (3, 2): set([7]), (0, 0): set([7]), (6, 6): set([8]), (5, 0): set([6]), (7, 1): set([7]), (4, 5): set([7]), (0, 4): set([9]), (5, 5): set([2]), (1, 4): set([5]), (6, 0): set([4]), (7, 5): set([9]), (2, 3): set([7]), (2, 1): set([9]), (8, 7): set([1]), (6, 8): set([7]), (4, 2): set([4]), (1, 0): set([8]), (0, 8): set([8]), (6, 5): set([5]), (3, 5): set([8]), (0, 1): set([3]), (8, 3): set([4]), (7, 0): set([1]), (4, 6): set([1]), (6, 7): set([2]), (8, 6): set([5]), (5, 2): set([3]), (6, 1): set([6]), (3, 1): set([1]), (8, 2): set([8]), (2, 4): set([8]), (3, 8): set([6]), (0, 6): set([4]), (1, 8): set([1]), (6, 2): set([9]), (4, 3): set([9]), (1, 7): set([7]), (0, 5): set([1]), (3, 4): set([3]), (0, 2): set([6]), (8, 4): set([7])})


		# sudoku = hw4.Sudoku(hw4.read_board("sudoku/medium3.txt")) 
		# sudoku.infer_improved()
		# self.assertEqual(sudoku.board, {(7, 3): set([7]), (4, 7): set([1]), (1, 3): set([5]), (4, 8): set([7]), (3, 0): set([2]), (2, 8): set([2]), (8, 0): set([3]), (7, 8): set([8]), (5, 4): set([9]), (0, 7): set([6]), (5, 6): set([4]), (2, 6): set([1]), (1, 6): set([8]), (5, 1): set([8]), (3, 7): set([8]), (0, 3): set([4]), (8, 5): set([2]), (2, 5): set([8]), (5, 8): set([3]), (4, 0): set([5]), (1, 2): set([2]), (7, 4): set([3]), (6, 4): set([1]), (3, 3): set([1]), (2, 0): set([7]), (8, 1): set([5]), (7, 6): set([5]), (4, 4): set([4]), (6, 3): set([6]), (1, 5): set([1]), (8, 8): set([1]), (7, 2): set([6]), (3, 6): set([9]), (2, 2): set([5]), (7, 7): set([9]), (5, 7): set([5]), (5, 3): set([2]), (4, 1): set([3]), (1, 1): set([6]), (2, 7): set([4]), (3, 2): set([7]), (0, 0): set([8]), (6, 6): set([3]), (5, 0): set([6]), (7, 1): set([2]), (4, 5): set([6]), (0, 4): set([2]), (5, 5): set([7]), (1, 4): set([7]), (6, 0): set([9]), (7, 5): set([4]), (2, 3): set([3]), (2, 1): set([9]), (8, 7): set([7]), (6, 8): set([4]), (4, 2): set([9]), (1, 0): set([4]), (0, 8): set([5]), (6, 5): set([5]), (3, 5): set([3]), (0, 1): set([1]), (8, 3): set([9]), (7, 0): set([1]), (4, 6): set([2]), (6, 7): set([2]), (8, 6): set([6]), (5, 2): set([1]), (6, 1): set([7]), (3, 1): set([4]), (8, 2): set([4]), (2, 4): set([6]), (3, 8): set([6]), (0, 6): set([7]), (1, 8): set([9]), (6, 2): set([8]), (4, 3): set([8]), (1, 7): set([3]), (0, 5): set([9]), (3, 4): set([5]), (0, 2): set([3]), (8, 4): set([8])})
		
		
	
	def test_infer_with_guessing(self):
		# sudoku = hw4.Sudoku(hw4.read_board("sudoku/hard1.txt")) 
		# sudoku.infer_with_guessing();
		# self.assertEqual(sudoku.board, {(7, 3): set([6]), (4, 7): set([9]), (1, 3): set([8]), (4, 8): set([5]), (3, 0): set([3]), (2, 8): set([3]), (8, 0): set([1]), (7, 7): set([5]), (0, 7): set([6]), (4, 6): set([4]), (0, 0): set([2]), (1, 6): set([9]), (5, 1): set([4]), (6, 2): set([3]), (3, 7): set([1]), (0, 3): set([7]), (8, 5): set([8]), (2, 5): set([2]), (5, 8): set([8]), (4, 0): set([6]), (1, 2): set([1]), (3, 8): set([6]), (3, 1): set([8]), (6, 7): set([8]), (3, 3): set([4]), (0, 2): set([5]), (1, 5): set([5]), (8, 1): set([5]), (7, 6): set([3]), (4, 4): set([8]), (6, 3): set([5]), (5, 6): set([7]), (7, 2): set([8]), (3, 6): set([2]), (2, 2): set([6]), (3, 4): set([5]), (0, 1): set([9]), (3, 5): set([9]), (4, 1): set([1]), (1, 1): set([3]), (6, 4): set([2]), (5, 4): set([1]), (2, 6): set([5]), (3, 2): set([7]), (5, 0): set([5]), (7, 1): set([2]), (4, 5): set([7]), (0, 4): set([4]), (6, 6): set([1]), (5, 5): set([6]), (1, 4): set([6]), (6, 0): set([7]), (7, 5): set([1]), (2, 3): set([1]), (2, 1): set([7]), (8, 7): set([7]), (8, 6): set([6]), (4, 2): set([2]), (1, 0): set([4]), (0, 8): set([1]), (6, 5): set([4]), (5, 3): set([2]), (2, 7): set([4]), (8, 3): set([9]), (7, 0): set([9]), (6, 8): set([9]), (5, 2): set([9]), (6, 1): set([6]), (5, 7): set([3]), (8, 2): set([4]), (0, 6): set([8]), (7, 4): set([7]), (2, 0): set([8]), (1, 8): set([7]), (8, 8): set([2]), (4, 3): set([3]), (1, 7): set([2]), (0, 5): set([3]), (7, 8): set([4]), (2, 4): set([9]), (8, 4): set([3])})
		
		# sudoku = hw4.Sudoku(hw4.read_board("sudoku/hard2.txt")) 
		# sudoku.infer_with_guessing()
		# self.assertEqual(sudoku.board, {(7, 3): set([4]), (4, 7): set([4]), (1, 3): set([3]), (4, 8): set([2]), (3, 0): set([1]), (2, 8): set([1]), (8, 0): set([9]), (7, 7): set([5]), (0, 7): set([2]), (4, 6): set([8]), (0, 0): set([8]), (1, 6): set([4]), (5, 1): set([8]), (6, 2): set([4]), (3, 7): set([3]), (0, 3): set([7]), (8, 5): set([2]), (2, 5): set([6]), (5, 8): set([7]), (4, 0): set([3]), (1, 2): set([6]), (3, 8): set([6]), (3, 1): set([7]), (6, 7): set([6]), (3, 3): set([2]), (0, 2): set([1]), (1, 5): set([1]), (8, 1): set([3]), (7, 6): set([2]), (4, 4): set([7]), (6, 3): set([9]), (5, 6): set([5]), (7, 2): set([7]), (3, 6): set([9]), (2, 2): set([3]), (3, 4): set([8]), (0, 1): set([5]), (3, 5): set([4]), (4, 1): set([6]), (1, 1): set([9]), (6, 4): set([1]), (5, 4): set([9]), (2, 6): set([7]), (3, 2): set([5]), (5, 0): set([4]), (7, 1): set([1]), (4, 5): set([5]), (0, 4): set([4]), (6, 6): set([3]), (5, 5): set([3]), (1, 4): set([2]), (6, 0): set([5]), (7, 5): set([8]), (2, 3): set([8]), (2, 1): set([4]), (8, 7): set([7]), (8, 6): set([1]), (4, 2): set([9]), (1, 0): set([7]), (0, 8): set([3]), (6, 5): set([7]), (5, 3): set([6]), (2, 7): set([9]), (8, 3): set([5]), (7, 0): set([6]), (6, 8): set([8]), (5, 2): set([2]), (6, 1): set([2]), (5, 7): set([1]), (8, 2): set([8]), (0, 6): set([6]), (7, 4): set([3]), (2, 0): set([2]), (1, 8): set([5]), (8, 8): set([4]), (4, 3): set([1]), (1, 7): set([8]), (0, 5): set([9]), (7, 8): set([9]), (2, 4): set([5]), (8, 4): set([6])})
		
		sudoku = hw4.Sudoku(hw4.read_board("sudoku/hard3.txt")) 
		sudoku.infer_with_guessing()
		#self.print_sudoku(sudoku)
		self.assertEqual(sudoku.board, {(7, 3): set([5]), (4, 7): set([2]), (1, 3): set([6]), (4, 8): set([1]), (3, 0): set([1]), (2, 8): set([3]), (8, 0): set([7]), (7, 8): set([7]), (7, 7): set([1]), (0, 7): set([4]), (6, 2): set([1]), (1, 6): set([1]), (5, 1): set([8]), (3, 7): set([9]), (0, 3): set([7]), (8, 5): set([8]), (2, 5): set([1]), (5, 8): set([4]), (4, 0): set([3]), (1, 2): set([3]), (7, 4): set([2]), (6, 7): set([6]), (3, 3): set([2]), (2, 0): set([6]), (8, 1): set([9]), (7, 6): set([9]), (4, 4): set([4]), (0, 0): set([8]), (6, 3): set([9]), (1, 5): set([2]), (7, 2): set([8]), (3, 6): set([8]), (2, 2): set([5]), (8, 6): set([4]), (5, 3): set([1]), (4, 1): set([6]), (1, 1): set([4]), (6, 4): set([7]), (5, 6): set([5]), (2, 6): set([2]), (3, 2): set([4]), (5, 0): set([2]), (2, 7): set([8]), (7, 1): set([3]), (4, 5): set([5]), (0, 4): set([5]), (6, 6): set([3]), (5, 5): set([9]), (1, 4): set([8]), (6, 0): set([5]), (7, 5): set([6]), (2, 3): set([4]), (2, 1): set([7]), (8, 7): set([5]), (6, 8): set([8]), (5, 4): set([6]), (4, 2): set([9]), (1, 0): set([9]), (0, 8): set([9]), (5, 7): set([3]), (6, 5): set([4]), (3, 5): set([7]), (0, 1): set([1]), (8, 3): set([3]), (7, 0): set([4]), (4, 6): set([7]), (5, 2): set([7]), (6, 1): set([2]), (3, 1): set([5]), (8, 2): set([6]), (2, 4): set([9]), (3, 8): set([6]), (0, 6): set([6]), (1, 8): set([5]), (8, 8): set([2]), (4, 3): set([8]), (1, 7): set([7]), (0, 5): set([3]), (3, 4): set([3]), (0, 2): set([2]), (8, 4): set([1])})
		
	def print_sudoku(self,sudoku):
		s = [[0]*9 for i in xrange(9)]
		for r, c in sudoku.board:
			s[r][c] = sudoku.board[(r,c)]
		for row in s:
			print row
		
if __name__ == '__main__':
	unittest.main()
