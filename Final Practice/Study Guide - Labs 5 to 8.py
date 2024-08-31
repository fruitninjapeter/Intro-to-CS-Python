# Lab 5: Iteration Patterns

# Used explicit loop for add_n_all
def add_n_all(numbers, n):
    result = [] # declare empty array
    for i in range(len(numbers)): # for loop considering all elements from numbers, from 0 to len(numbers)
        result.append(numbers[i] + n) # adds an element to "result" which is the element from numbers plus n
    return result


print("Adding 6 to the list of [4, 3, 2] results in... " + str(add_n_all([4, 3, 2], 6)))


# Used list comprehension for are_positive
def are_positive(numbers):
    return [x for x in numbers if x > 0]


print("From the list of [0, -5, 2], the positive number is... " + str(are_positive([0, -5, 2])))

# Lab 6: While Loops, Counting, Folds


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


# Shortest version of lists of three (one liner, list comprehension)
def groups_of_three(list):
    return [list[i:i+3] for i in range(0, len(list), 3)]
    # List slicing ^                    ^ considers first(0) to third(2) elements in list


def while_version(items):
   result = []
   count = len(items) - 1
   while count >= 0:
      result.append(items[count])
      count -= 1
   return result


# Lab 7: Character and String Manipulation, Command-Line Arguments

def is_lower_101(char): # Test if a character is lowercase
    return 97 <= ord(char) <= 112


def char_rot_13(char): # returns rot-13 encoding of a character
    if 65 <= ord(char) <= 77 or 97 <= ord(char) <= 109:
        return chr(ord(char) + 13)
    if 77 <= ord(char) <= 90 or 110 <= ord(char) <= 122:
        return chr(ord(char) - 13)
    return char


def str_rot_13(string): # returns rot-13 encoding of a string
    return ''.join([char_rot_13(c) for c in string])


def str_translate_101(string, old, new): # replaces certain characters in string with new characters
    slist = list(string)
    for i in range(0, len(string)):
        if ord(slist[i-1]) == ord(old):
            slist[i-1] = new
    return ''.join(slist)


# Lab 8: Convert and Exceptions

def float_default(string, fail):
    try:
        return float(string)
    except:
        return fail