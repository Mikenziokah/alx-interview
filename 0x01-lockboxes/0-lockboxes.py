#!/usr/bin/python3
""" lockboxes challenge"""


def canUnlockAll(boxes):
    """ finding the open lockboxes"""
    opened = {0}  # Initialize with box 0 as opened.
    keys = set(boxes[0])  # Start with keys from the first box.

    while True:
        progress = False

        for key in list(keys):  # Convert to list to avoid runtime modification issues.
            if key < len(boxes) and key not in opened:
                opened.add(key)
                keys.update(boxes[key])  # Add new keys from the opened box.
                progress = True

        if not progress:
            break

    return len(opened) == len(boxes)


def main():
    """ edge casses"""
    test_cases = [
        [[1], [2], [3], []],
        [[1, 2], [3], [0], []],
        [[1, 3], [3, 0, 1], [2], [0]],
    ]

    for i, boxes in enumerate(test_cases):
        result = canUnlockAll(boxes)
        print("Test Case {}: {}".format(i + 1, result))

if __name__ == "__main__":
    main()
