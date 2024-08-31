import unittest
from fold import *
from point import *


class TestCases(unittest.TestCase):

   def test_sum1(self):
      self.assertAlmostEqual(sum([5,5,5]), 15)

   def test_sum2(self):
      self.assertAlmostEqual(sum([8,3,-2]), 9)

   def test_smallest1(self):
      self.assertAlmostEqual(index_of_smallest([5,7,1]),1)

   def test_smallest2(self):
      self.assertAlmostEqual(index_of_smallest([]), -1)

   def test_smallest3(self):
      self.assertAlmostEqual(index_of_smallest([-420, 69, 420, -419.999, -1]), -420)

   def test_origin1(self):
      Points1 = [Point(5, 5), Point(4, 7), Point(3, 4)]
      Origin1 = Point(0, 0)
      self.assertAlmostEqual(nearest_origin(Points1, Origin1), 5)

   def test_origin2(self):
      Points2 = []
      Origin2 = Point(0, 0)
      self.assertAlmostEqual(nearest_origin(Points2, Origin2), -1)

   def test_origin3(self):
      Points3 = [Point(-30,5), Point(420,420), Point(20.5,20)]
      Origin3 = Point(20,20)
      self.assertAlmostEqual(nearest_origin(Points3, Origin3), 0.5)


# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

