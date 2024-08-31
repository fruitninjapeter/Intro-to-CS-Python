import utility


# Used list comprehension for are_positive
def are_positive(numbers):
    return [x for x in numbers if x > 0]


# Used explicit for loop for are_greater_than
def are_greater_than(numbers, n):
    result = []
    for i in range(len(numbers)):
        if numbers[i] > n:
            result.append(numbers[i])
    return result


class Point():
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return utility.epsilon_equal(self.x, other.x) and \
               utility.epsilon_equal(self.y, other.y)


def are_in_first_quadrant(points):
    #return [point for point in points if point.x > 0 and point.y > 0]
    result = []
    for i in range(len(points)):
        if points[i].x > 0 and points[i].y > 0:
            result.append(points[i])
    return result
