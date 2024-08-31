from collisions import *


def cast_ray(ray, sphere_list):
    rayint = find_intersection_points(sphere_list, ray)
    if rayint == []:
        return Color(255, 255, 255)
    else:
        nearest = 0
        for i in range(len(rayint)):
            if length_vector(vector_from_to(ray.pt, rayint[i][1])) < length_vector(
                    vector_from_to(ray.pt, rayint[nearest][1])):  # [i][i of tuple]
                nearest = i
            return rayint[nearest][0].color  # return sphere part, color part.


def cast_all_rays(min_x, max_x, min_y, max_y, width, height, eye_point, sphere_list):
    xinterval = (max_x - min_x) / width
    yinterval = (max_y - min_y) / height

    image_file = open("imagepart2.ppm", "w")

    image_file.write("P3\n")
    image_file.write("%d %d\n" % (width, height)) # insert integer values
    image_file.write("255\n")

    for i in range(height):
        y = max_y - (i * yinterval)
        for j in range(width):
            x = min_x + (j * xinterval)
            dir = vector_from_to(eye_point, Point(x,y,0))
            RayCheck = Ray(eye_point, dir)
            Colors = cast_ray(RayCheck, sphere_list)
            image_file.write("%d %d %d\n" % (Colors.r, Colors.g, Colors.b)) # color values
    image_file.close()
