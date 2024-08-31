from cast import *
from vector_math import *

# Eye at <0.0, 0.0, -14.0>.
# A sphere at <1.0, 1.0, 0.0> with radius 2.0.
# A sphere at <0.5, 1.5, -3.0> with radius 0.5.
# A viewport with minimum x of -10, maximum x of 10, minimum y of -7.5, maximum y of 7.5, width of
# 512, and height of 384.

xmin = -10
xmax = 10
ymin = -7.5
ymax = 7.5
width = 512
height = 384
sphere1 = Sphere(Point(1, 1, 0), 2)
sphere2 = Sphere(Point(.5, 1.5, -3), .5)
sphere_list = [sphere1, sphere2]
eye = Point(0, 0, -14)
cast_all_rays(xmin, xmax, ymin, ymax, width, height, eye, sphere_list)