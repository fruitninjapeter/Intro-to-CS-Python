from cast import *
import unittest


class TestCases(unittest.TestCase):

    def test_castray1(self):
        Ray1 = Ray(Point(-5, -8, 3), Vector(-4, -43, 10))
        SphereList1 = [Sphere(Point(100, 420, 88), 0.001)]
        self.assertEqual(cast_ray(Ray1,SphereList1), False)

    def test_castray2(self):
        Ray2 = Ray(Point(0.0, 0.0, 0.0), Vector(2.0, 2.0, 5.0 / 3.0))
        sphere1 = Sphere(Point(5.0, 0.0, 0.0), 5.0)
        sphere2 = Sphere(Point(11.0, 6.0, 5.0), 5.0)
        sphere3 = Sphere(Point(17.0, 12.0, 10.0), 5.0)
        SphereList2 = [sphere1, sphere2, sphere3]
        self.assertEqual(cast_ray(Ray2, SphereList2), True)


if __name__ == '__main__':
    unittest.main()