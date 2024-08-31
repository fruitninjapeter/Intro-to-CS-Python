def for_version(items):
   result = []
   for i in range(len(items) - 1, -1, -1):
      result.append(items[i])
   return result


def while_version(items):
   result = []
   count = len(items) - 1
   while count >= 0:
      result.append(items[count])
      count -= 1
   return result
