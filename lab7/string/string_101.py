def char_rot_13(char): # returns rot-13 encoding of a character
    if 65 <= ord(char) <= 77 or 97 <= ord(char) <= 109:
        return chr(ord(char) + 13)
    if 77 <= ord(char) <= 90 or 110 <= ord(char) <= 122:
        return chr(ord(char) - 13)
    return char


def str_rot_130(string): # returns rot-13 encoding of a string
    slist = list(string)
    for i in range(0, len(string)):
        slist[i-1] = char_rot_13(slist[i-1])
    return ''.join(slist)


def str_rot_13(string): # returns rot-13 encoding of a string
    return ''.join([char_rot_13(c) for c in string])


def str_translate_101(string, old, new): # replaces certain characters in string with new characters
    slist = list(string)
    for i in range(0, len(string)):
        if ord(slist[i-1]) == ord(old):
            slist[i-1] = new
    return ''.join(slist)
