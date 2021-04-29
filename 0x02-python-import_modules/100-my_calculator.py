#!/usr/bin/python3
def handler_error(number_one, number_two):
    print("Unknown operator. Available operators: +, -, * and /")
    exit(1)
    return None

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys

    first = 0
    sys.argv.pop(first)
    length = len(sys.argv)
    if length != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
        quit()

    argv = sys.argv;
    number_one = int(argv.pop(first))
    operation = argv.pop(first)
    number_two = int(argv.pop(first))
    handler_operation = None
    resolve = None
    operations = {
        '+': add,
        '-': sub,
        '/': div,
        '*': mul
    }

    handler_operation = operations.get(operation, handler_error)
    resolve = handler_operation(number_one, number_two)
    print("%d %s %d = %d" % (number_one, str(operation), number_two, resolve))

