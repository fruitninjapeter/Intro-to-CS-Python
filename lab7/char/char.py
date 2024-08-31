def is_lower_101(char): # Test if a character is lowercase
    return 97 <= ord(char) <= 112


def char_rot_13(char): # returns rot-13 encoding of a character
    if 65 <= ord(char) <= 77 or 97 <= ord(char) <= 109:
        return chr(ord(char) + 13)
    if 77 <= ord(char) <= 90 or 110 <= ord(char) <= 122:
        return chr(ord(char) - 13)
    return char
