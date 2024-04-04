#!/usr/bin/python3
""" a method that detrmines if a given dataset represents a UTF-8 encording
"""
def validUTF8(data):
    """ function to validate encoding
    """

    num_counts = 0

    series_1 = 1 << 7
    series_2 = 1 << 6

    for x in data:

        serie_counts = 1 << 7

        if num_counts == 0:

            while series_count & x:
                num_counts += 1
                num_count = num_count >>1

                if num_counts == 0:
                    continue

                if num_counts == 1 and num_counts > 4:
                    return False

                else:
                    if not (x & series_1 and not (x & series_2)):
                        return False

                    num_counts -= 1

                    if num_counts == 0:
                        return True

                    return False
