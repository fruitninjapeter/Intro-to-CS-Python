from vector_math import *
from math import sqrt


def sphere_intersection_point(ray, sphere):

    StartRaySphere = diff_point(ray.pt,sphere.center)
    A = dot_vector(ray.dir,ray.dir)
    B = dot_vector(scale_vector(StartRaySphere, 2), ray.dir)
    C = dot_vector(StartRaySphere,StartRaySphere) - (sphere.radius ** 2)

    # Quadratic Formula checks
    determinant = (B ** 2) - (4 * A * C)
    if determinant > 0:
        t1 = ((-B) + sqrt(determinant)) / (2 * A)
        t2 = ((-B) - sqrt(determinant)) / (2 * A)
        if (t1 >= 0 and t2 >= 0):
            if t1 > t2:
                return trans_point(ray.pt, scale_vector(ray.dir, t2))
            else:
                return trans_point(ray.pt, scale_vector(ray.dir, t1))
        elif (t1 > 0 or t2 > 0):
            if t1 > 0:
                return trans_point(ray.pt, scale_vector(ray.dir, t1))
            else:
                return trans_point(ray.pt, scale_vector(ray.dir, t2))
    return None


def find_intersection_points(sphere_list, ray):
    result = []
    for i in range(len(sphere_list)):
        if sphere_intersection_point(ray, sphere_list[i]) != None:
            result.append( (sphere_list[i],sphere_intersection_point(ray,sphere_list[i])) )
    return result


def sphere_normal_at_point(sphere, point):
    center_to_surface = vector_from_to(sphere.center,point)
    return norm_vector(center_to_surface)