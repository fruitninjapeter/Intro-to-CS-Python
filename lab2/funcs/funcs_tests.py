import unittest
import funcs


class TestCases(unittest.TestCase):
    def test_f1(self):
        self.assertEqual(funcs.f(5), 185)

    def test_f2(self):
        self.assertEqual(funcs.f(2), 32)

    def test_g1(self):
        self.assertEqual(funcs.g(3, 2), 13)

    def test_g2(self):
        self.assertEqual(funcs.g(2, 6), 40)

    def test_hypotenuse1(self):
        self.assertEqual(funcs.hypotenuse(3, 4), 5)

    def test_hypotenuse2(self):
        self.assertEqual(funcs.hypotenuse(6, 8), 10)

    def test_is_positive1(self):
        self.assertTrue(funcs.is_positive(3))
        # self.assertFalse(funcs.is_positive(3))

    def test_is_positive2(self):
        # self.assertTrue(funcs.is_positive(-6))
        self.assertFalse(funcs.is_positive(-6))


# Run the unit tests.
if __name__ == '__main__':
    unittest.main()
