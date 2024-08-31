from math import sqrt


def sum(list):
    total = 0
    for i in range(len(list)):
        add = list[i]
        total += add
    return total


def index_of_smallest(list):
    result = -1
    for i in range(len(list)):
        if i == 0:     # First element of list
            result = list[i]
        if list[i] < result:    # replace result with list[i] if it is smaller
            result = list[i]
    return result


def distance(p, q): # made a distance function between 2D points p and q
    return sqrt(((q.x-p.x)**2) + ((q.y-p.y)**2))


def nearest_origin(list, origin):
    result = -1
    for i in range(len(list)):
        if i == 0:
            result = distance(list[i], origin)
        if distance(list[i], origin) < result:
            result = distance(list[i], origin)
    return result
