#!/usr/bin/python3
def roman_to_int(roman_string):
    if isinstance(roman_string, str) is False:
        return 0
    romansum = []
    num = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)
    for i in range(0, len(roman_string), 1):
        if roman_string[i] in num:
            romansum.append(num[roman_string[i]])
            if i + 1 <= len(romansum) and romansum[i] < romansum[i + 1]:
                romansum[i] = -romansum[i]
    return sum(romansum)
