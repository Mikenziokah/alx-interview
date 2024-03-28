#!/usr/bin/python3

import sys


def print_codes(status_codes, total_file_size):
    """ function to print status codes and their total file
        size in ascending order
    """
    print("File size: {}".format(total_file_size))
    for key, val in sorted(status_codes.items()):
        if val != 0:
            print("{}: {}".format(key, val))


total_file_size = 0
counter = 0
status_codes = {"200": 0,
                "301": 0,
                "400": 0,
                "401": 0,
                "403": 0,
                "404": 0,
                "405": 0,
                "500": 0}

try:
    for line in sys.stdin:
        parsed_line = line.split()  # ✄ trimming
        parsed_line = parsed_line[::-1]  # inverting

        if len(parsed_line) > 2:
            counter += 1

            if counter <= 10:
                total_file_size += int(parsed_line[0])  # file size
                code = parsed_line[1]  # status code

                if code in status_codes.keys():
                    status_codes[code] += 1

            if counter == 10:
                print_codes(status_codes, total_file_size)
                counter = 0

finally:
    print_codes(status_codes, total_file_size)
