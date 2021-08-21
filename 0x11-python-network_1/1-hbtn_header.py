#!/usr/bin/python3
"""
Python script that takes in a URL and prints header X-Request-Id
"""

from urllib.request import urlopen
from sys import argv

if __name__ == "__main__":
    with urlopen(argv[1]) as response:
        headers_like_dict = dict(response.getheaders())
        print(headers_like_dict.get('X-Request-Id'))
