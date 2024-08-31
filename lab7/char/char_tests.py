import unittest
from char import *


class TestChar(unittest.TestCase):

   def test_lower1(self):
      self.assertEqual(is_lower_101('d'), True)

   def test_lower2(self):
      self.assertEqual(is_lower_101('G'), False)

   def test_lower3(self):
      self.assertEqual(is_lower_101('8'), False)

   def test_rot13_1(self):
      self.assertEqual(char_rot_13('A'), 'N')

   def test_rot13_2(self):
      self.assertEqual(char_rot_13('z'), 'm')

   def test_rot13_3(self):
      self.assertEqual(char_rot_13('$'), '$')


if __name__ == '__main__':
   unittest.main()

