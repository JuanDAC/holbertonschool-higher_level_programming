#!/usr/bin/python3
print_sorted_dictionary = __import__('6-print_sorted_dictionary').print_sorted_dictionary

a_dictionary = { 'language': "C", 'Number': 89, 'track': "Low level", 'ids': [1, 2, 3] }
print_sorted_dictionary(a_dictionary)
print("-" * 50)
a_dictionary = { 'az': "3", 'ab': 2, 'aaz': "1", 'ids': [1, 2, 3] }
print_sorted_dictionary(a_dictionary)
print("-" * 50)
a_dictionary = None
print_sorted_dictionary(a_dictionary)
print("-" * 50)

