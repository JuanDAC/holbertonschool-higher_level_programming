#!/usr/bin/python3
for number in range(0, 100):
    print("{:d}".format(number), end='\n' if number == 99 else ", ")
