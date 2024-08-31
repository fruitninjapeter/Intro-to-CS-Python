import unittest
import conditional


class TestCases(unittest.TestCase):

   def test_2max1(self):
      self.assertEqual(conditional.max_101(420,69),420)
      self.assertEqual(conditional.max_101(2.1111,2.1110),2.1111)

   def test_2max2(self):
      self.assertTrue(conditional.max_101(3,4) == 4)
      self.assertFalse(conditional.max_101(12,13) == 12)

   def test_3max1(self):
      self.assertEqual(conditional.max_of_three(1,2,3), 3)
      self.assertEqual(conditional.max_of_three(2,3.5,4), 4)

   def test_3max2(self):
      self.assertTrue(conditional.max_of_three(10,13,14) == 14)
      self.assertFalse(conditional.max_of_three(19,42,1) == 1)

   def test_rental0dollars(self):
      self.assertEqual(conditional.rental_late_fee(0), 0)

   def test_rental5dollars(self):
      self.assertEqual(conditional.rental_late_fee(6), 5)

   def test_rental7dollars(self):
      self.assertEqual(conditional.rental_late_fee(14), 7)

   def test_rental19dollars(self):
      self.assertEqual(conditional.rental_late_fee(18), 19)

   def test_rental100dollars(self):
      self.assertEqual(conditional.rental_late_fee(69), 100)

if __name__ == '__main__':
   unittest.main()

