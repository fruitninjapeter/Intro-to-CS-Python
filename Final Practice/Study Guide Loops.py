# Loops: While and For statements, converting between them using "count"
# For these functions, items would be the given list, we want to return the items list but backwards
def for_version(items):
   result = []
   for i in range(len(items) - 1, -1, -1):
      result.append(items[i])
   return result


treasures = [6,5,4,3,2,1,0]
print("Backwards list of treasures using for_version is... " + str(for_version(treasures)))


def while_version(items):
    result = []
    count = len(items) - 1 # Cannot be just len(items)...
    while count >= 0: # likewise cannot be count > 0...
        result.append(items[count])
        count -= 1
    return result
# ... because lists first element is the "0th", so if list has 5 elements its highest is called the "4th".


print("Backwards list of treasures using while_version is... " + str(while_version(treasures)))