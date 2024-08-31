import data
import unittest


class TestCases(unittest.TestCase):

    def test_Point1(self):
        p1 = data.Point(3, 4, 5)
        self.assertAlmostEqual(p1.x, 3)
        self.assertAlmostEqual(p1.y, 4)
        self.assertAlmostEqual(p1.z, 5)

    def test_Point2(self):
        p2 = data.Point(-9, 14, 0)
        self.assertAlmostEqual(p2.x, -9)
        self.assertAlmostEqual(p2.y, 14)
        self.assertAlmostEqual(p2.z, 0)

    def test_Vector1(self):
        v1 = data.Vector(3, 6, 1)
        self.assertAlmostEqual(v1.x, 3)
        self.assertAlmostEqual(v1.y, 6.0)
        self.assertAlmostEqual(v1.z, 1)

    def test_Vector2(self):
        v2 = data.Vector(-10, 2.6, 6.66)
        self.assertAlmostEqual(v2.x, -10)
        self.assertAlmostEqual(v2.y, 2.6)
        self.assertAlmostEqual(v2.z, 6.66)

    def test_Ray1(self):
        r1 = data.Ray(data.Point(0, 0, 0), data.Vector(0, 1, 0))
        self.assertAlmostEqual(r1.pt.x, 0)
        self.assertAlmostEqual(r1.pt.y, 0)
        self.assertAlmostEqual(r1.pt.z, 0)
        self.assertAlmostEqual(r1.dir.x, 0)
        self.assertAlmostEqual(r1.dir.y, 1)
        self.assertAlmostEqual(r1.dir.z, 0)

    def test_Ray2(self):
        r1 = data.Ray(data.Point(420, 69, 13), data.Vector(3, 666, 8))
        self.assertAlmostEqual(r1.pt.x, 420)
        self.assertAlmostEqual(r1.pt.y, 69)
        self.assertAlmostEqual(r1.pt.z, 13)
        self.assertAlmostEqual(r1.dir.x, 3)
        self.assertAlmostEqual(r1.dir.y, 666)
        self.assertAlmostEqual(r1.dir.z, 8)

    def test_Sphere1(self):
        s1 = data.Sphere(data.Point(10.0, 20.0, 30.0), 9.0)
        self.assertAlmostEqual(s1.center.x, 10.0)
        self.assertAlmostEqual(s1.center.y, 20.0)
        self.assertAlmostEqual(s1.center.z, 30.0)
        self.assertAlmostEqual(s1.radius, 9.0)

    def test_Sphere2(self):
        s2 = data.Sphere(data.Point(-5.0, -25.0, 125.0), 0.5)
        self.assertAlmostEqual(s2.center.x, -5.0)
        self.assertAlmostEqual(s2.center.y, -25.0)
        self.assertAlmostEqual(s2.center.z, 125.0)
        self.assertAlmostEqual(s2.radius, 0.5)


if __name__ == '__main__':
    unittest.main()