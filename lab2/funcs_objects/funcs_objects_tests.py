import unittest
import objects
import funcs_objects


class TestCases(unittest.TestCase):

   def test_Point1(self):
      p1 = objects.Point(1,2)
      self.assertEqual(p1.x,1)
      self.assertEqual(p1.y,2)

   def test_Point2(self):
      p2 = objects.Point(3,4)
      self.assertEqual(p2.x,3)
      self.assertEqual(p2.y,4)

   def test_Circle1(self):
      circle1 = objects.Circle(objects.Point(2,69),8)
      self.assertEqual(circle1.center.x, 2)
      self.assertEqual(circle1.center.y, 69)
      self.assertEqual(circle1.radius, 8)

   def test_Circle2(self):
      circle2 = objects.Circle(objects.Point(420,-9001),12)
      self.assertEqual(circle2.center.x, 420)
      self.assertEqual(circle2.center.y, -9001)
      self.assertEqual(circle2.radius, 12)

   def test_distance1(self):
      distance1 = funcs_objects.distance(objects.Point(10,10),objects.Point(10,20))
      self.assertEqual(distance1,10)

   def test_distance2(self):
      distance2 = funcs_objects.distance(objects.Point(5,5),objects.Point(10,10))
      self.assertEqual(distance2,7.0710678118654755)

   def test_circles_overlap1(self):
      circle3 = objects.Circle(objects.Point(1,1), 3)
      circle4 = objects.Circle(objects.Point(5,5), 1)
      self.assertFalse(funcs_objects.circles_overlap(circle3, circle4))

   def test_circles_overlap2(self):
      circle5 = objects.Circle(objects.Point(-3,2), 30)
      circle6 = objects.Circle(objects.Point(10,8), 15)
      self.assertTrue(funcs_objects.circles_overlap(circle5, circle6))

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

