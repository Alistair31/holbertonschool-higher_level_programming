#!/usr/bin/python3
"""
Docstring for python-test_driven_development.5-text_indentation
"""


def text_indentation(text):
    """
    Prints text with 2 new lines after each '.', '?' and ':'.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    result = ""
    i = 0

    while i < len(text):
        result += text[i]

        if text[i] in ".?:":
            result += "\n\n"
            i += 1
            while i < len(text) and text[i] == " ":
                i += 1
            continue

        i += 1

    print(result, end="")
