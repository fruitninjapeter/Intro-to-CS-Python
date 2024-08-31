import math

def f(x):
    return 7*x*x + 2*x

def g(x,y):
    return x*x + y*y

def hypotenuse(side1,side2):
    return math.sqrt(side1*side1 + side2*side2)

def is_positive(n):
    return n>0