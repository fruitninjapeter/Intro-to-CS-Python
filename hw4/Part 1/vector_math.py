from math import sqrt
from data import *


def scale_vector(vector, scalar):
    return Vector(vector.x * scalar, vector.y * scalar, vector.z * scalar)


def dot_vector(vector1, vector2):
    return (vector1.x * vector2.x) + (vector1.y * vector2.y) + (vector1.z * vector2.z)


def length_vector(vector):
    return sqrt(vector.x ** 2 + vector.y ** 2 + vector.z ** 2)


def norm_vector(vector):
    mag = length_vector(vector)
    return Vector(vector.x/mag, vector.y/mag, vector.z/mag)


def diff_point(p1, p2):
    return Vector(p1.x - p2.x, p1.y - p2.y, p1.z - p2.z)


def diff_vector(v1, v2):
    return Vector(v1.x - v2.x, v1.y - v2.y, v1.z - v2.z)


def trans_point(point,vector):
    return Point(point.x + vector.x, point.y + vector.y, point.z + vector.z)


def vector_from_to(from_point,to_point):
    return Vector(to_point.x - from_point.x,
                  to_point.y - from_point.y,
                  to_point.z - from_point.z)