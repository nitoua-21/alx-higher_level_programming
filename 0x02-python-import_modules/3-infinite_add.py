#!/usr/bin/python3
if __name__ == '__main__':
    import sys

    count = len(sys.argv)
    total = 0
    if count > 1:
        for i in range(1, count):
            total += int(sys.argv[i])
    print(total)
