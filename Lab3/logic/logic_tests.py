import unittest
import logic


class TestCases(unittest.TestCase):

   def test_even1(self):
      self.assertTrue(logic.is_even(-2))
      self.assertFalse(logic.is_even(1))

   def test_even2(self):
      self.assertEqual(logic.is_even(101), False)
      self.assertEqual(logic.is_even(60), True)

   def test_interval1(self):
      self.assertTrue(logic.in_an_interval(8))
      self.assertFalse(logic.in_an_interval(11))
      self.assertTrue(logic.in_an_interval(18.99999999999))
      self.assertFalse(logic.in_an_interval(19.0000000001))

   def test_interval2(self):
      self.assertEqual(logic.in_an_interval(69.4206913), True)
      self.assertEqual(logic.in_an_interval(101.0101010101), True)


# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

