import unittest
from convert import *


class TestConvert(unittest.TestCase):

   def test_convert1(self):
      self.assertEqual(float_default("12.66", "You failed"), 12.66)

   def test_convert2(self):
      self.assertEqual(float_default("Boobies", "You failed LMAO get rekt"), "You failed LMAO get rekt")


if __name__ == '__main__':
   unittest.main()

