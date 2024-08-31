from cast import *
from data import *

xmin = -10
xmax = 10
ymin = -7.5
ymax = 7.5
width = 512
height = 384
sphere1 = Sphere(Point(1, 1, 0), 2, Color(0, 0, 255), Finish(.2))
sphere2 = Sphere(Point(.5, 1.5, -3), .5, Color(255, 0, 0), Finish(.4))
sphere_list = [sphere2, sphere1]
eye = Point(0, 0, -14)
ambient = Color(255,255,255)
cast_all_rays(xmin, xmax, ymin, ymax, width, height, eye, sphere_list, ambient)
