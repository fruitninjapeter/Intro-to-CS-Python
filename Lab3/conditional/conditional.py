def max_101(n1,n2):
    if n1 > n2:
        return n1
    else:
        return n2


def max_of_three(n1,n2,n3):
    if n1 > n2 and n1 > n3:
        return n1
    elif n2 > n1 and n2 > n3:
        return n2
    else:
        return n3


def rental_late_fee(days):
    if days <= 0:
        fee = 0
    elif 0 < days and days <= 9:
        fee = 5
    elif 9 < days and days <= 15:
        fee = 7
    elif 15 < days and days <= 24:
        fee = 19
    else:
        fee = 100
    return fee
