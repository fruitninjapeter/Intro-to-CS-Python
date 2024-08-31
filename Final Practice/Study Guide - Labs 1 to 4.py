from math import sqrt


# Lab 1: Classes


class Vehicle:
    def __init__(self, wheels, fuel, doors, roof):
        self.wheels = wheels
        self.fuel = fuel
        self.doors = doors
        self.roof = roof


car = Vehicle(4, 100, 2, False)
print("The vehicle has " + str(car.wheels) + " wheels!")

# Lab 2: Functions


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Circle:
    def __init__(self, center, r):
        self.center = center
        self.radius = r


def distance(p, q):
    return sqrt(((q.x - p.x)**2) + ((q.y - p.y)**2))


def circles_overlap(c1, c2):  # Circle Overlap = distance < combined radius = True or False
    return distance(c1.center, c2.center) <= (c1.radius + c2.radius)


circle1 = Circle(Point(1, 1), 3)
circle2 = Circle(Point(5, 5), 1)
print("The circles listed overlap? " + str(circles_overlap(circle1, circle2)))

circle3 = Circle(Point(-3, 2), 30)
circle4 = Circle(Point(10, 8), 15)
print("The circles listed overlap? " + str(circles_overlap(circle3, circle4)))

# Lab 3: Conditionals


def is_even(n): # Returns true or false for whether or not a number is even
    return (n % 2) == 0


print("The number 3 is even? " + str(is_even(3)))


def max_of_three(n1,n2,n3):
    if n1 > n2 and n1 > n3:
        return n1
    elif n2 > n1 and n2 > n3:
        return n2
    else:
        return n3


print("The max of 6, -6, and 6.01 is " + str(max_of_three(6, -6, 6.01)))

# Lab 4: Conditionals and Lists


def poly_mult2(l1,l2):
    list3 = []
    list3.append(l1[0]*l2[0])
    list3.append(l1[0]*l2[1] + l1[1]*l2[0])
    list3.append(l1[1]*l2[1] + l1[2]*l2[0] + l1[0]*l2[2])
    list3.append(l1[2]*l2[1] + l1[1]*l2[2])
    list3.append(l1[2]*l2[2])
    return list3


list1 = [1, 2, 1] # x^2 + 2x + 1
list2 = poly_mult2(list1, list1) # (x^2 + 2x + 1)^2
print("New list is... " + str(list2))