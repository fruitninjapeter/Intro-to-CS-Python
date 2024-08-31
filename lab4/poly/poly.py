def poly_add2(list1,list2):
    list3 = []
    list3.append(list1[0] + list2[0])
    list3.append(list1[1] + list2[1])
    list3.append(list1[2] + list2[2])
    return list3


def poly_mult2(l1,l2):
    list3 = []
    list3.append(l1[0]*l2[0])
    list3.append(l1[0]*l2[1] + l1[1]*l2[0])
    list3.append(l1[1]*l2[1] + l1[2]*l2[0] + l1[0]*l2[2])
    list3.append(l1[2]*l2[1] + l1[1]*l2[2])
    list3.append(l1[2]*l2[2])
    return list3