#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = (number % 10 if number >= 0 else (number * -1) % 10 * -1)

print("Last digit %d of %d and is " % (number, last_digit), end='')
if last_digit > 5:
    print("greater than 5")
elif last_digit == 0:
    print("0")
else:
    print("less than 6 and not 0")
