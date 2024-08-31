import math


def distance(p, q):
    return math.sqrt(((q.x - p.x)**2) + ((q.y - p.y)**2))


def circles_overlap(c1,c2):
    return distance(c1.center,c2.center) <= (c1.radius + c2.radius)
    # Circle Overlap? = distance < combined radius = True