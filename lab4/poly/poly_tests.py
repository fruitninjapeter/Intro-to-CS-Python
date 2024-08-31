import poly
import unittest


class TestPoly(unittest.TestCase):

   def test_addtest1(self):
      list1 = [3,4,5]
      list2 = [6,7,8]
      list3 = poly.poly_add2(list1,list2)
      self.assertEqual(list3,[9,11,13])

   def test_addtest2(self):
      list4 = [-3,-2,-5]
      list5 = [-1,7,5]
      list6 = poly.poly_add2(list4,list5)
      self.assertEqual(list6,[-4,5,0])

   def test_multtest1(self):
      list7 = [1, 2, 1] # x^2 + 2x + 1
      list8 = poly.poly_mult2(list7, list7) # (x^2 + 2x + 1)^2
      self.assertEqual(list8, [1, 4, 6, 4, 1]) # x^4 + 4x^3 + 6x^2 + 4x + 1

   def test_multtest2(self):
      list9 = [3, -2, 4] # 4x^2 - 2x + 3
      list10 = [-1, 5, 2] # 2x^2 + 5x - 1
      list11 = poly.poly_mult2(list9, list10) # (4x^2 - 2x + 3)*(2x^2 + 5x - 1)
      self.assertEqual(list11, [-3, 17, -8, 16, 8]) # 8x^4 + 16x^3 - 8x^2 + 17x - 3

if __name__ == '__main__':
    unittest.main()
