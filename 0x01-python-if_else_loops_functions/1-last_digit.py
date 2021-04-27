#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = (number if number >= 0 else (number * -1)) % 2
if (last_digit > 5):
    print("Last digit {:d} of {:d} and is greater than 5".format(number, last_digit))
elif (last_digit == 0):
    print("Last digit {:d} of {:d} and is 0".format(number, last_digit))
else:
    print("Last digit {:d} of {:d} and is less than 6 and not 0".format(number, last_digit))

