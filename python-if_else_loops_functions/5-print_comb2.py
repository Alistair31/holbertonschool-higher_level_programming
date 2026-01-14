#!/usr/bin/python3
for c in range(0, 99):
    print("{0:02}, ".format(c), end="")
    if c == 98:
        print("99".format(c))
