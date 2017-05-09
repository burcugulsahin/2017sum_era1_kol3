import unittest
from matrix import Matrix

class testing_init(unittest.TestCase):
	def setUp(self):
		self.t1 = [[1,1,1],[2,2,2],[3,4,5,6,7,8,9]]

	def test_init(self):
		m1 = Matrix(self.t1)
		self.assertEqual(self.t1[0],m1.rows[0])
		self.assertEqual(self.t1[1],m1.rows[1])
		self.assertEqual(self.t1[2],m1.rows[2])

class testing_simple_sum(unittest.TestCase): 
	def setUp(self):
		self.t1 = [[1,1,1],[2,2,2]]
		self.tr = [[2,2,2],[4,4,4]]

	def test_init(self):
		m1 = Matrix(self.t1)
		m2 = Matrix(self.t1)
		m3 = m1 + m2
		self.assertEqual(self.tr,m3.rows)

class testing_output(unittest.TestCase): 
	def setUp(self):
		self.t1 = [[1,2,1],[3,3,3],[5,5,5]]
		self.output = "|1 2 1|\n|3 3 3|\n|5 5 5|\n"

	def test_init(self):
		m1 = Matrix(self.t1)
		output_m1 = str(m1)
		self.assertEqual(self.output,output_m1)

class testing_direct_sum(unittest.TestCase): 
	def setUp(self):
		self.t1 = [[1,2,1],[3,3,3],[5,5,5]]
		self.total = [[2,3,2],[4,4,4],[6,6,6]]

	def test_init(self):
		m1 = Matrix(self.t1)
		total_m1 = m1+1
		self.assertEqual(self.total,total_m1.rows)

class testing_transpose(unittest.TestCase): 
	def setUp(self):
		self.t1 = [[1,2,1],[3,3,3],[5,5,5]]
		self.transpose = [[1,3,5],[2,3,5],[1,3,5]]

	def test_init(self):
		m1 = Matrix(self.t1)
		transpose_m1 = m1.transpose
		self.assertEqual(self.transpose,transpose_m1.rows)

class testing_string(unittest.TestCase): 
	def setUp(self):
		self.t1 = [['A','B'],['Hello','World']]
		self.t2 = [['Selam','canim'],['C','D']]
		self.t3 = [['A Selam','B canim'],['Hello C','World D']]

	def test_init(self):
		m1 = Matrix(self.t1)
		m2 = Matrix(self.t2)
		m3 = m1+" "+m2
		self.assertEqual(self.t3,m3.rows)

class testing_shape(unittest.TestCase):
	def setUp(self):
		self.t1 = [[1,2,1],[3,3,3]]
		self.shape_0 = 2
		self.shape_1 = 3

	def test_init(self):
		m1 = Matrix(self.t1)
		shape_m1_0 = m1.shape[0]
		shape_m1_1 = m1.shape[1]
		self.assertEqual(self.shape_0,shape_m1_0)
		self.assertEqual(self.shape_1,shape_m1_1)


class testing_iter(unittest.TestCase):
	def setUp(self):
		self.t1 = [[1,2,1],[3,3,3],[5,5,5]]

	def test_init(self):
		index = 0
		m1 = Matrix(self.t1)
		for iter in m1:
			self.assertEqual(self.t1[index],iter)
			index += 1

if __name__ == '__main__':
	unittest.main()