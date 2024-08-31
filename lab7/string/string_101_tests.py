import unittest
from string_101 import *


class TestString(unittest.TestCase):

   def test_string101_1(self):
      self.assertEqual(str_rot_13('Lbhe zbz!'),'Your mom!')

   def test_string101_2(self):
      self.assertEqual(str_rot_13('YZNB trg qrfgeblrq lbh cbbcbburnq!!!'),
                       'LMAO get destroyed you poopoohead!!!')

   def test_translate1(self):
      self.assertEqual(str_translate_101('Boobies','o','u'),'Buubies')

   def test_translate2(self):
      self.assertEqual(str_translate_101('Smells loke fosh','o','I'),'Smells lIke fIsh')


if __name__ == '__main__':
   unittest.main()

