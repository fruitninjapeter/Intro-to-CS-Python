import math


# Used list comprehension for square_all
def square_all(numbers):
    return [i * i for i in numbers]


# Used explicit loop for add_n_all
def add_n_all(numbers, n):
    result = [] # declare empty array
    for i in range(len(numbers)): # for loop considering all elements from numbers, from 0 to len(numbers)
        result.append(numbers[i] + n) # adds an element to "result" which is the element from numbers plus n
    return result


class Point():
    def __init__(self, x, y): # initialize variables of class
        self.x = x
        self.y = y


def distance(p,q): # made a distance function between 2D points p and q
    return math.sqrt(((q.x-p.x)**2) + ((q.y-p.y)**2))


def distance_all(points, origin):
    result = [] # declare empty array
    for i in range(len(points)): # for loop considering all points in the array, from 0 to len(points)
        # adds an element which is the rounded distance between a point(p) and assigned origin(q)
        result.append(round(distance(points[i],origin), 2))
    return result
