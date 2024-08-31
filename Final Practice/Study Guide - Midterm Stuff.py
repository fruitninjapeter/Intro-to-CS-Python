from math import sqrt


def listnum(list, number):
    return list.count(number)


list1 = [4, 2, 5, 7, 2, 1]
number1 = 2
print(listnum(list1,number1))

list2 = [1, 2, 3, 4]
number2 = 0
print(listnum(list2,number2))


def perimeter(ptlist): # works for polygon containing n number of points
    p = 0
    for i in range(len(ptlist)):
        if i == 0:
            pass
        else:
            dist = sqrt((ptlist[i - 1].y - ptlist[i].y) ** 2 + (ptlist[i - 1].x - ptlist[i].x) ** 2)
            p += dist
    p += (sqrt((ptlist[0].y - ptlist[-1].y) ** 2 + (ptlist[0].x - ptlist[-1].x) ** 2))
    # last point and first point
    return p