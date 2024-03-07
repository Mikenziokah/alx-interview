#!/usr/bin/python3
"""
pascals triangle implementation
"""


def pascal_triangle(n):
    """ creates afunction that returnsa lists of lists of
    intergers representing the pascal triangle
    """
    triangle = []
    if n > 0:
        for x in range (1, n + 1):
            row = []
            y = 1
            for z in range (1, x + 1):
                row.append(y)
                y = y * (x - z) // z
            triangle.append(row)
    return triangle
