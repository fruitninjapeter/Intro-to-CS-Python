# Strings: converting strings (immutable) to lists and vice-versa to "change" a string

def str_translate_101(string, old, new): # replaces certain characters in string with new characters
    slist = list(string)
    for i in range(0, len(string)):
        if ord(slist[i-1]) == ord(old): # ord() is the number that python designates to each character
            slist[i-1] = new
    return ''.join(slist) # joins list together


old = "buubies"
print("Change u from buubies to o results in " + str_translate_101(old, "u", "o") + "!")


def str_translate_2(string, old1, new1, old2, new2): # This list can change 2 characters instead of one
    slist = list(string)
    for i in range(0, len(string)):
        if ord(slist[i - 1]) == ord(old1):
            slist[i - 1] = new1
        if ord(slist[i - 1]) == ord(old2):
            slist[i - 1] = new2
    return ''.join(slist)


text1 = "HELLO DUM HOES"
x = text1.lower()
print(x) # lower() lowercase's a given string


text2 = "I like cock"
y = text2.replace("cock", "pussy")
print(y) # replace() replaces designated string with new string


text3 = "                kekw              "
z = text3.strip()
print("I like to", z, "ye dolt") # strip() removes spaces at the beginning and end of string


text4 = "Hi I am Lord Lard"
a = text4.split()
print(a) # split() splits a string into words, with each being an element in a list


tuple = ("Yo", "what's", "up")
b = ''.join(tuple)
print(b) # join() combines elements of a tuple into a string assigning whatever you want as a separator
