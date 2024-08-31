# Mutable data type means that a python object of this type can be modified.
# An immutable object cannot be modified.
# Lists are mutable.
a = [1, "kek", 3, 4, 5]
a[1] = 2
print(str(a))
# Tuples are immutable

# Dictionaries are used to store data values in key:value pairs.
Dictionary = {"Best Champ": "Sion", "Name?": "Bluehawkstriker", "kek?": "w"}
print(Dictionary)
# Printing "Name?" value of dictionary.
print(Dictionary["Name?"])
# Dictionaries are mutable.
Dictionary["Name?"] = "Yo mama"
print(Dictionary["Name?"])

# Sets are used to store multiple items in a single variable
Set = {"Your", "mums", "a hoe"}
print(Set)
# Sets are mutable, but it's strange since there aren't index values for us to easily change whats in a set
# Sets are unordered and not indexed

# MUTABLE: Lists, Dictionaries, Sets
# IMMUTABLE: Tuples

# List Slicing
exlist = [0, 1, 2, 3, 4, 5]
a = exlist[0:3] # items start from 0 to 2
print(str(a))
b = exlist[2:] # items start from 2 (third element) to rest of array
print(str(b))
c = exlist[:4] # items from beginning through 3rd element
print(str(c))
d = exlist[:] # copies whole array
print(str(d))
e = exlist[-1] # last item in array
print(str(e))
f = exlist[-2] # 2nd to last item in array

# 'in' operator checks whether or not a value is in a list
#list1=[1,2,3,4,5]
#list2=[6,7,8,9]
#for item in list1:
#    if item in list2:
#        print("overlapping")
#else:
#    print("not overlapping")