#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    value = 0
    first = 0
    sys.argv.pop(first)
    for current_number_string in sys.argv:
        value = value + int(current_number_string)
    print("{:d}".format(value))
