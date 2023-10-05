#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    arg_count = len(sys.argv) - 1
    print("{} argument".format(arg_count), end='')
    print('{}'.format('' if arg_count == 1 else 's'), end='')
    print('', end='.' if arg_count == 0 else ':')
    print()
    for i in range(arg_count):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
