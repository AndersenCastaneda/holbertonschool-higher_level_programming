#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    length = len(sys.argv)
    add = 0

    for i in range(1, length):
        add += int(sys.argv[i])

    print(add)
