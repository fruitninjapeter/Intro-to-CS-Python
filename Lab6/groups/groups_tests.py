import unittest
from groups import *


class TestGroups(unittest.TestCase):

   def assertListAlmostEqual(self, l1, l2):
      self.assertEqual(len(l1), len(l2))
      for el1, el2 in zip(l1, l2):
         self.assertAlmostEqual(el1, el2)

   def test_threegroup1(self):
      self.assertListAlmostEqual(groups_of_3([420,-69,55,666,23]),[[420,-69,55],[666,23]])

   def test_threegroup2(self):
      self.assertAlmostEqual(groups_of_3([1,2,3,4,5,6,7,8]),[[1, 2, 3], [4, 5, 6], [7, 8]])

   def test_threegroup3(self):
      self.assertAlmostEqual(groups_of_3([69,69]),[[69,69]])


if __name__ == '__main__':
   unittest.main()
