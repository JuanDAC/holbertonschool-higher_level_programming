#!/usr/bin/python3
import sys

def safe_function(fct, *args):
    try:
        resolve = fct(*args)
    except Exception as ex:
        print(ex, file=sys.stderr)
        return None
    else:
        return resolve
