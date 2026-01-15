#!/usr/bin/python3
for c in range(0, 10):
    for d in range(0, 10):
        if c < d:
            if c == 8 and d == 9:
                print("89")
            else:
                print("{}{}".format(c, d), end=", ")
