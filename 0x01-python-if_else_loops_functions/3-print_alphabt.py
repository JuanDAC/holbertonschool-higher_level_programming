#!/usr/bin/python3
list_alphabet = list(range(97, 100)) \
    + list(range(102, 112)) \
    + list(range(104, 123))
print("".join(map(chr, list_alphabet)), end="")
