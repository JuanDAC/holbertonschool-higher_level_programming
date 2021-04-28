#!/usr/bin/python3
def uppercase(string):
    string_new = ""
    for character in string:
        if ord(character) >= 97 and ord(character) <= 122:
            string_new += "{:c}".format(ord(character) - 32)
        else:
            string_new += "{:s}".format(character)
    print("{:s}".format(string_new))

