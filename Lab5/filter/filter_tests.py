import filter
import unittest


class TestCases(unittest.TestCase):

    def test_are_positive1(self):
        posnumblist1 = filter.are_positive([10,-2,5,-1])
        self.assertEqual(posnumblist1, [10, 5])

    def test_are_positive2(self):
        posnumblist2 = filter.are_positive([0,-1,-6,3])
        self.assertEqual(posnumblist2, [3])

    def test_are_greater_than1(self):
        greaterthan1 = filter.are_greater_than([4,1,3,8],1)
        self.assertEqual(greaterthan1, [4, 3, 8])

    def test_are_greater_than2(self):
        greaterthan2 = filter.are_greater_than([0,-4,9,12,3],2)
        self.assertEqual(greaterthan2, [9, 12, 3])

    def test_are_in_first_quadrant1(self):
        pointlist1 = [filter.Point(2,1),filter.Point(3,-2),filter.Point(10,9)]
        firstquadrant1 = filter.are_in_first_quadrant(pointlist1)
        #self.assertEqual(firstquadrant1[0].x, 2)
        #self.assertEqual(firstquadrant1[0].y, 1)
        #self.assertEqual(firstquadrant1[1].x, 10)
        #self.assertEqual(firstquadrant1[1].y, 9)
        self.assertEqual(firstquadrant1,[filter.Point(2,1),filter.Point(10,9)])

    def test_are_in_first_quadrant2(self):
        pointlist2 = [filter.Point(-2, 7), filter.Point(8, 0.01), filter.Point(-1, -1), filter.Point(0.03,0.5)]
        firstquadrant2 = filter.are_in_first_quadrant(pointlist2)
        #self.assertEqual(firstquadrant2[0].x, 8)
        #self.assertEqual(firstquadrant2[0].y, 0.01)
        #self.assertEqual(firstquadrant2[1].x, 0.03)
        #self.assertEqual(firstquadrant2[1].y, 0.5)
        self.assertEqual(firstquadrant2,[filter.Point(8, 0.01),filter.Point(0.03,0.5)])


if __name__ == '__main__':
    unittest.main()