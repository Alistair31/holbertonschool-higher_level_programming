#!/usr/bin/python3
from sys import argv
print("{} arguments.".format(len(argv) - 1))
for i in range(1, len(argv)):
    if (len(argv) == 1) != "":
        print("{}: {}".format(i, argv[i]))
    else:
        print(".")
