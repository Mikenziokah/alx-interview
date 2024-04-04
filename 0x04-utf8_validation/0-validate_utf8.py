#!/usr/bin/python3
""" a method that detrmines if a given dataset represents a UTF-8 encording
"""
def validUTF8(data):
    """Function to validate UTF-8 encoding."""
    num_bytes = 0
    series_1 = 1 << 7
    series_2 = 1 << 6

    for x in data:
        series_count = 1 << 7

        if num_bytes == 0:
            while series_count & x:
                num_bytes += 1
                series_count = series_count >> 1

            if num_bytes == 0:
                continue

            if num_bytes == 1 or num_bytes > 4:
                return False

        else:
            if not (x & series_1 and not (x & series_2)):
                return False

            num_bytes -= 1

    return num_bytes == 0
