from data import *
from collisions import *
from vector_math import *
import unittest


class TestCases(unittest.TestCase):

    def test_sphereintpoint1(self):
        Ray1 = Ray(Point(0,0,0), Vector(3,0,0))
        Sphere1 = Sphere(Point(4,0,0), 1)
        self.assertAlmostEqual(sphere_intersection_point(Ray1,Sphere1), Point(3,0,0))

    def test_sphereintpoint2(self):
        Ray2 = Ray(Point(-5,-8,3), Vector(0,0,100))
        Sphere2 = Sphere(Point(-5,-8,3), 3)
        self.assertAlmostEqual(sphere_intersection_point(Ray2,Sphere2), Point(-5,-8,6))

    def test_sphereintpoint3(self):
        Ray3 = Ray(Point(-5,-8,3), Vector(-4,-43,10))
        Sphere3 = Sphere(Point(100,420,88), 0.001)
        self.assertAlmostEqual(sphere_intersection_point(Ray3,Sphere3), None)

    def test_find_intersection_points_1(self):
        sphere1 = Sphere(Point(8,0,0),2)
        sphere2 = Sphere(Point(4,0,0),1)
        ray1 = Ray(Point(0,0,0),Vector(10,0,0))
        self.assertAlmostEqual(find_intersection_points([sphere1,sphere2],ray1),
                               [(sphere1,Point(6,0,0)),
                                (sphere2,Point(3,0,0))])

    def test_find_intersection_points_2(self):
        ray2 = Ray(Point(0.0, 0.0, 0.0), Vector(2.0, 2.0, 5.0 / 3.0))
        sphere1 = Sphere(Point(5.0, 0.0, 0.0), 5.0)
        sphere2 = Sphere(Point(11.0, 6.0, 5.0), 5.0)
        sphere3 = Sphere(Point(17.0, 12.0, 10.0), 5.0)
        sphere_list = [sphere1, sphere2, sphere3]
        test2 = find_intersection_points(sphere_list, ray2)
        self.assertEqual(test2, [(sphere1, Point(0.0, 0.0, 0.0)),
                                     (sphere2, Point(6.0, 6.0, 5.0)),
                                     (sphere3, Point(12.0, 12.0, 10.0))])

    def test_sphere_normal_1(self):
        sphere = Sphere(Point(5.0, 0.0, 0.0), 5.0)
        pt = Point(10.0, 0.0, 0.0)
        test1 = sphere_normal_at_point(sphere, pt)
        self.assertEqual(test1, Vector(1.0, 0.0,0.0))

    def test_sphere_normal_2(self):
        sphere = Sphere(Point(5.0, 3.0, 2.0), 3.3)
        pt = Point(1.7, 3.0, 2.0)
        test2 = sphere_normal_at_point(sphere, pt)
        self.assertEqual(test2, Vector(-1.0, 0.0, 0.0))


if __name__ == '__main__':
    unittest.main()