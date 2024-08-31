import map
import unittest


class TestCases(unittest.TestCase):

    def test_squared_numbers1(self):
        squared_numbers1 = map.square_all([1,2,3,4,5])
        self.assertEqual(squared_numbers1, [1,4,9,16,25])

    def test_squared_numbers2(self):
        squared_numbers2 = map.square_all([0,3,-10,6,3])
        self.assertEqual(squared_numbers2,[0,9,100,36,9])

    def test_add_n_all1(self):
        newnumbers1 = map.add_n_all([5,6,7,8,9], 5)
        self.assertEqual(newnumbers1, [10, 11, 12, 13, 14])

    def test_add_n_all2(self):
        newnumbers2 = map.add_n_all([60,411,657], 9)
        self.assertEqual(newnumbers2, [69, 420, 666])

    def test_distance_all1(self):
        distances1 = map.distance_all([map.Point(3,4),map.Point(20,2),map.Point(2,2)],map.Point(0,0))
        self.assertEqual(distances1, [5.0, 20.1, 2.83])

    def test_distance_all2(self):
        distances2 = map.distance_all([map.Point(6,8), map.Point(7,3), map.Point(1,0)], map.Point(1,0))
        self.assertEqual(distances2, [9.43, 6.71, 0.0])

# assertAlmostEqual can be used instead of rounding in the function
if __name__ == '__main__':
    unittest.main()