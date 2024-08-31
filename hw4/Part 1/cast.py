from collisions import *


def cast_ray(ray, sphere_list):
    rayint = find_intersection_points(sphere_list,ray)
    if len(rayint) != 0:
        return True
    return False


def cast_all_rays(min_x, max_x, min_y, max_y, width, height, eye_point, sphere_list):
    xinterval = (max_x - min_x) / width
    yinterval = (max_y - min_y) / height

    image_file = open("imagepart1.ppm", "w")

    image_file.write("P3\n")
    image_file.write("%d %d\n" % (width, height)) # insert integer values
    image_file.write("255\n")

    for i in range(height):
        y = max_y - (i * yinterval)
        for j in range(width):
            x = min_x + (j * xinterval)
            # cast a ray through each point
            dir = vector_from_to(eye_point, Point(x,y,0)) # cast a ray through each point
            RayCheck = Ray(eye_point, dir)
            if cast_ray(RayCheck, sphere_list):
                image_file.write("0 0 0\n")
            else:
                image_file.write("255 255 255\n")
    image_file.close()
