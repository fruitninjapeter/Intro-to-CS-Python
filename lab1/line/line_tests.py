import unittest
import line

class LineTests(unittest.TestCase):
   def test_line(self):
      a = line.line(420,69,32,64)
      self.assertEqual(a.x1, 420)
      self.assertEqual(a.y1, 69)
      self.assertEqual(a.x2, 32)
      self.assertEqual(a.y2, 64)
      b = line.line(1,2,3,4)
      self.assertEqual(b.x1, 1)
      self.assertEqual(b.y1, 2)
      self.assertEqual(b.x2, 3)
      self.assertEqual(b.y2, 4)

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

