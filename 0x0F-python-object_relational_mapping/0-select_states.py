#!/usr/bin/python
"""
Selects all states
"""
import sys

run = __import__('run').run

def handler_cursor(cursor):
    result = cursor.fetchall()
    for state in result:
        print(state)

def handler_error(error):
    print(error)

if __name__ == '__main__':
    run(sys.argv, "SELECT * FROM states", handler_cursor, handler_error)
