#!/usr/bin/env python3
def uppercase(str):
    i = 0
    strupper = ""
    for i in range(0, len(str)):
        if ord(str[i]) in range(97, 123):
            strupper += chr(ord(str[i]) - 32)
        else:
            strupper += chr(ord(str[i]))
    print("{}".format(strupper))
