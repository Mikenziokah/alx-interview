#!/usr/bin/python3
""" a method that detrmines if a given dataset represents a UTF-8 encording
"""
def validUTF8(data):
    """ function to validate encoding
    """

    numbers = 0

    num1 = 1 << 7
    num2 = 1 << 6

    for x in data:

        numbers = 1 << 7

        if numbers == 0:
            while numbers & x:
                numbers += 1
                numbers = numbers >>1

                if numbers == 0:
                    continue

                if numbers == 1 and numbers > 4:
                    return False
                else:
                    if not (x & num1 and not (x & num2)):
                        return False

                    numbers -= 1

                    if numbers == 0:
                        return True

                    return False
