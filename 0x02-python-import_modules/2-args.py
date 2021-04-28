#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    value = len(sys.argv) - 1
    print("{:d} argument{:s}{:s}".format(
        value,
        's' if value != 1 else '',
        ':' if value != 0 else '.'
    ))
    for i in range(1, len(sys.argv)):
        print("{:d}: {:s}".format(i, sys.argv[i]))
