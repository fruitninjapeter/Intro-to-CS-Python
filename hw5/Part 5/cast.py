from collisions import *


def cast_ray(ray, sphere_list, ambient, light, eye_point):
    rayint = find_intersection_points(sphere_list, ray)
    if rayint == []:
        return Color(255, 255, 255)
    else:
        nearest = 0
        for i in range(len(rayint)):
            if length_vector(vector_from_to(ray.pt, rayint[i][1])) < length_vector(
                    vector_from_to(ray.pt, rayint[nearest][1])):  # [i][i of tuple]
                nearest = i
        r = rayint[nearest][0].color.r * rayint[nearest][0].finish.ambient * (ambient.r/255)
        g = rayint[nearest][0].color.g * rayint[nearest][0].finish.ambient * (ambient.r/255)
        b = rayint[nearest][0].color.b * rayint[nearest][0].finish.ambient * (ambient.r/255)
        # Part 4 Stuff
        N = sphere_normal_at_point(rayint[nearest][0], rayint[nearest][1])
        Pe = trans_point(rayint[nearest][1], scale_vector(N, 0.01))  # Step 1
        light_dir = norm_vector(vector_from_to(Pe, light.pt))  # Step 2
        visible = dot_vector(light_dir, N)  # Step 3
        ray_col = Ray(Pe, vector_from_to(Pe, light.pt))  # Step 4

        if visible > 0:
            c1 = find_intersection_points(sphere_list, ray_col)
            if c1 == []:
                r += light.color.r * visible * rayint[nearest][0].finish.diffuse * rayint[nearest][0].color.r
                g += light.color.g * visible * rayint[nearest][0].finish.diffuse * rayint[nearest][0].color.g
                b += light.color.b * visible * rayint[nearest][0].finish.diffuse * rayint[nearest][0].color.b
        # Part 5 Stuff
        LdotN = dot_vector(light_dir, N)
        refvector = diff_vector(light_dir, scale_vector(N, 2*LdotN))
        Vdir = norm_vector(vector_from_to(eye_point, Pe))
        SpecInt = dot_vector(refvector, Vdir)
        SpecIntRough = SpecInt ** (1/(rayint[nearest][0].finish.roughness))

        if SpecInt > 0:
            r += light.color.r * rayint[nearest][0].finish.specular * SpecIntRough
            g += light.color.g * rayint[nearest][0].finish.specular * SpecIntRough
            b += light.color.b * rayint[nearest][0].finish.specular * SpecIntRough
        return Color(r, g, b)


def cast_all_rays(min_x, max_x, min_y, max_y, width, height, eye_point, sphere_list, ambient, light):
    xinterval = (max_x - min_x) / width
    yinterval = (max_y - min_y) / height

    image_file = open("imagepart5.ppm", "w")

    image_file.write("P3\n")
    image_file.write("%d %d\n" % (width, height))   # insert integer values
    image_file.write("255\n")

    for i in range(height):
        y = max_y - (i * yinterval)
        for j in range(width):
            x = min_x + (j * xinterval)
            dir = vector_from_to(eye_point, Point(x,y,0))
            RayCheck = Ray(eye_point, dir)
            Colors = cast_ray(RayCheck, sphere_list, ambient, light, eye_point)
            image_file.write("%d %d %d\n" % (Colors.r, Colors.g, Colors.b))  # color values
    image_file.close()
