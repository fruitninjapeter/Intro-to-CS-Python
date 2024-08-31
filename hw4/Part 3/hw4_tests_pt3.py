from cast import *
from data import *
import unittest


class TestCases(unittest.TestCase):

    def test_castray1(self):
        Ray1 = Ray(Point(-5, -8, 3), Vector(-4, -43, 10))
        SphereList1 = [Sphere(Point(100, 420, 88), 0.001, Color(56,72,33), Finish(1))]
        self.assertEqual(cast_ray(Ray1,SphereList1, Color(255,255,255)), Color(255,255,255))

    def test_castray2(self):
        Ray2 = Ray(Point(0, 0, 0), Vector(5, 0, 0))
        sphere1 = Sphere(Point(2, 0, 0), 1.5, Color(255, 0, 0),Finish(.5))
        sphere2 = Sphere(Point(3, 0, 0), 2, Color(0, 0, 255),Finish(1))
        SphereList2 = [sphere1, sphere2]
        self.assertEqual(cast_ray(Ray2, SphereList2, Color(30,0,0)), Color(15, 0, 0))


if __name__ == '__main__':
    unittest.main()