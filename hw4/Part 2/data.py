from utility import *


class Point():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __eq__(self, other):
        if other is None:
            return False
        return epsilon_equal(self.x, other.x) and \
               epsilon_equal(self.y, other.y) and \
               epsilon_equal(self.z, other.z)


class Vector():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __eq__(self, other):
        return epsilon_equal(self.x, other.x) and \
               epsilon_equal(self.y, other.y) and \
               epsilon_equal(self.z, other.z)


class Ray():
    def __init__(self, pt, dir):
        self.pt = pt
        self.dir = dir

    def __eq__(self, other):
        return (self.pt == other.pt) and (self.dir == other.dir)


class Sphere():
    def __init__(self, center, radius, color):
        self.center = center
        self.radius = radius
        self.color = color

    def __eq__(self, other):
        return (self.center == other.center) and \
               epsilon_equal(self.radius, other.radius) and (self.color == other.color)


class Color:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def __eq__(self, other):
        r_eq = epsilon_equal(self.r, other.r)
        g_eq = epsilon_equal(self.g, other.g)
        b_eq = epsilon_equal(self.b, other.b)
        return r_eq and g_eq and b_eq
