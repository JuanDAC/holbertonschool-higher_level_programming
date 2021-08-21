#!/usr/bin/python3
"""
Python script that takes in a URL and an email, sends a POST
"""

from urllib.request import urlopen
from urllib.parse import urlencode
from sys import argv

if __name__ == "__main__":
    data = urlencode({"email": argv[2]}).encode('ascii')
    with urlopen(argv[1], data) as response:
        print(response.data)
