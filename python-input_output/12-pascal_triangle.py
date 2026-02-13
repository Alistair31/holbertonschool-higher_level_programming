#!/usr/bin/python3
"""
python-input_output.12-pascal_triangle
"""


def pascal_triangle(n):
    """
    pascal_triangle

    :param n: size of triangle
    """
    if n <= 0:
        return []
    whole_list = [[1]]
    pre_list = [1]
    for i in range(n - 1):
        new_list = [1]
        for j in range(i):
            new_list.append(pre_list[j] + pre_list[j + 1])
        new_list.append(1)
        whole_list.append(new_list)
        pre_list = new_list
    return whole_list
