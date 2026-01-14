#!/usr/bin/python3
for c in range(0, 100):
    if c == 99:
        print("{0}".format(c))
    print("{0:02}, ".format(c), end="")
