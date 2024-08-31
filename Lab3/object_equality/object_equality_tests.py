import unittest
import point


class TestCases(unittest.TestCase):

   def test_point_one(self):
      pt1 = point.Point(1, 2)
      self.assertEqual(pt1.x, 1)
      self.assertEqual(pt1.y, 2)

   def test_point_two(self):
      pt2 = point.Point(-4.7, 19.2)
      self.assertEqual(pt2.x, -4.7)
      self.assertEqual(pt2.y, 19.2)

   def test_equality1(self):
      pt1 = point.Point(1, 2)
      pt2 = point.Point(1, 2)
      pt3 = point.Point(2, 1)
      self.assertTrue(pt1 == pt2)
      self.assertFalse(pt1 == pt3)
      self.assertFalse(pt3 == pt2)

   def test_equality2(self):
      pt4 = point.Point(3,-7)
      pt5 = point.Point(3,-7)
      pt6 = point.Point(420,69)
      self.assertTrue(pt4 == pt5)
      self.assertEqual(pt6,point.Point(420,69))
      self.assertFalse(pt6 == pt5)
      self.assertEqual(pt4, pt5)


# Run the unit tests.
if __name__ == '__main__':
   unittest.main()
