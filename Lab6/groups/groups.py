def groups_of_3(l):
    result = []
    sublist = []
    for i in range(len(l)):
        if len(sublist) < 3:
            sublist.append(l[i])
        else:
            result.append(sublist)
            sublist = []
            sublist.append(l[i])
    result.append(sublist)
    return result


# Shorter version
def groups_of_three(lst):
    result = []
    for i in range(0, len(lst), 3):
        result.append(lst[i:i+3])
    return result


# Even shorter version (one liner, list comprehension)
def groups_of_ree(lst):
    return [lst[i:i+3] for i in range(0, len(lst), 3)]
