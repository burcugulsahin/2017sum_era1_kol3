    class MatrixTests(unittest.TestCase):
 
    def testAdd(self):
         m1 = Matrix.fromList([[1, 2, 3], [4, 5, 6]])
         m2 = Matrix.fromList([[7, 8, 9], [10, 11, 12]])        
         m3 = m1 + m2
         self.assertTrue(m3 == Matrix.fromList([[8, 10, 12], [14,16,18]]))
 
     def testSub(self):
        m1 = Matrix.fromList([[1, 2, 3], [4, 5, 6]])
         m2 = Matrix.fromList([[7, 8, 9], [10, 11, 12]])        
         m3 = m2 - m1
         self.assertTrue(m3 == Matrix.fromList([[6, 6, 6], [6, 6, 6]]))
 
     def testMul(self):
         m1 = Matrix.fromList([[1, 2, 3], [4, 5, 6]])
         m2 = Matrix.fromList([[7, 8], [10, 11], [12, 13]])
         self.assertTrue(m1 * m2 == Matrix.fromList([[63, 69], [150, 165]]))
         self.assertTrue(m2*m1 == Matrix.fromList([[39, 54, 69], [54, 75, 96], [64, 89, 114]]))
 
 
     def testId(self):
 
         m1 = Matrix.makeId(10)
         m2 = Matrix.makeRandom(4, 10)
         m3 = m2*m1
         self.assertTrue(m3 == m2)
 
 if __name__ == "__main__":
     unittest.main()
     
     
     
     
     
     
     
     
     
     
     
     
