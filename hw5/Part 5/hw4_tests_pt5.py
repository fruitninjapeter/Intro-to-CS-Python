from cast import *
from data import *
import unittest


class TestCases(unittest.TestCase):

    def test_castray1(self):
        Ray1 = Ray(Point(-5, -8, 3), Vector(-4, -43, 10))
        SphereList1 = [Sphere(Point(100, 420, 88), 0.001, Color(56,72,33), Finish(1, 1, .4, .09))]
        light1 = Light(Point(-100, 100, -100), Color(1.5, 1.5, 1.5))
        castray1 = cast_ray(Ray1,SphereList1, Color(255,255,255), light1, Point(6,6,6))
        self.assertEqual(castray1, Color(255,255,255))

    def test_castray2(self):
        Ray2 = Ray(Point(-5, -8, 3), Vector(-4, -43, 10))
        SphereList2 = [Sphere(Point(100, 300, 88), 0.001, Color(56,72,33), Finish(1, 1, .65, .25))]
        ambient = Color(1.0, 1.0, 0.0)
        light2 = Light(Point(-100, 100, -100), Color(1.5, 1.5, 1.5))
        castray2 = cast_ray(Ray2, SphereList2, ambient, light2, Point(3,6,1))
        self.assertEqual(castray2, Color(255,255,255))


if __name__ == '__main__':
    unittest.main()