from vector_math import *
from data import *
import unittest


class TestCases(unittest.TestCase):

    def test_equalityPoint1(self):
        pt1 = Point(4, -5.2, 0)
        pt2 = Point(4, -5.2, 0)
        pt3 = Point(0, 0, 0)
        self.assertTrue(pt1 == pt2)
        self.assertFalse(pt1 == pt3)
        self.assertFalse(pt2 == pt3)

    def test_equalityPoint2(self):
        pt4 = Point(3, -7, 10)
        pt5 = Point(3, -7, 10)
        pt6 = Point(420, 69, 13)
        self.assertTrue(pt4 == pt5)
        self.assertEqual(pt6, Point(420, 69, 13))
        self.assertFalse(pt6 == pt5)

    def test_equalityVector1(self):
        v1 = Vector(1,2.42,3)
        v2 = Vector(1,2.42,3)
        v3 = Vector(6,6,6)
        self.assertTrue(v1 == v2)
        self.assertFalse(v1 == v3)
        self.assertFalse(v2 == v3)

    def test_equalityVector2(self):
        v1 = Vector(-42,13,666)
        v2 = Vector(7,0,1.5)
        self.assertFalse(v1 == v2)

    def test_equalityRay1(self):
        r1 = Ray(Point(1,2,3), Vector(3,3,3))
        r2 = Ray(Point(1, 2, 3), Vector(3, 3, 3))
        self.assertTrue(r1 == r2)

    def test_equalityRay2(self):
        r1 = Ray(Point(-3,666,42), Vector(5,3,1))
        r2 = Ray(Point(1, 2, 3), Vector(3, 3.44, 3))
        self.assertFalse(r1 == r2)

    def test_equalitySphere1(self):
        s1 = Sphere(Point(0, 0, 0), 1.5)
        s2 = Sphere(Point(0, 0, 0), 1.5)
        self.assertTrue(s1 == s2)

    def test_equalitySphere2(self):
        s1 = Sphere(Point(35, 2.6, 8), 7)
        s2 = Sphere(Point(0, 0, 0), 1.5)
        self.assertFalse(s1 == s2)

    def test_scaleVector1(self):
        v1 = Vector(1,2,3)
        self.assertAlmostEqual(scale_vector(v1,2), Vector(2,4,6))

    def test_scaleVector2(self):
        v2 = Vector(-2.7,6.9,42)
        self.assertAlmostEqual(scale_vector(v2,10), Vector(-27,69,420))

    def test_dotVector1(self):
        v1 = Vector(3,4,5)
        v2 = Vector(1,1,1)
        self.assertAlmostEqual(dot_vector(v1,v2),12)

    def test_dotVector2(self):
        v1 = Vector(3.4, 4.8, 12)
        v2 = Vector(1, 2, 1)
        self.assertAlmostEqual(dot_vector(v1, v2), 25)

    def test_lengthVector1(self):
        v = Vector(5,5,5)
        self.assertAlmostEqual(length_vector(v),8.66025403784)

    def test_lengthVector2(self):
        v = Vector(3.0,4.0,5.0)
        self.assertAlmostEqual(length_vector(v), 7.07106781187)

    def test_normVector1(self):
        v = Vector(1,0,0)
        self.assertAlmostEqual(norm_vector(v),Vector(1,0,0))

    def test_normVector2(self):
        v = Vector(0, 4, 1)
        self.assertAlmostEqual(norm_vector(v), Vector(0, 0.97014250014, 0.24253562503))

    def test_diffPoint1(self):
        p1 = Point(0, 0, 0)
        p2 = Point(420, 69, 13)
        self.assertAlmostEqual(diff_point(p1, p2), Vector(-420, -69, -13))

    def test_diffPoint2(self):
        p1 = Point(40, 1313, 6.66)
        p2 = Point(27, 13, -0.03)
        self.assertAlmostEqual(diff_point(p1, p2), Vector(13, 1300, 6.69))

    def test_diffVector1(self):
        v1 = Vector(0,0,1)
        v2 = Vector(5,0,2)
        self.assertAlmostEqual(diff_vector(v1,v2), Vector(-5,0,-1))

    def test_diffVector2(self):
        v1 = Vector(6,6,6)
        v2 = Vector(-3,0,2)
        self.assertAlmostEqual(diff_vector(v1,v2), Vector(9,6,4))

    def test_transPoint1(self):
        p = Point(4,2,1)
        v = Vector(2,3,4)
        self.assertAlmostEqual(trans_point(p,v), Point(6,5,5))

    def test_transPoint2(self):
        p = Point(9.5,3.3,4.2)
        v = Vector(10, 662.7, -4)
        self.assertAlmostEqual(trans_point(p, v), Point(19.5, 666, 0.2))

    def test_vectorfromto1(self):
        p1 = Point(0,0,0)
        p2 = Point(420,69,666)
        self.assertAlmostEqual(vector_from_to(p1,p2), Vector(420, 69, 666))

    def test_vectorfromto2(self):
        p1 = Point(8.1, -4.4, 82)
        p2 = Point(428.1, 0, 95)
        self.assertAlmostEqual(vector_from_to(p1, p2), Vector(420, 4.4, 13))


if __name__ == '__main__':
    unittest.main()