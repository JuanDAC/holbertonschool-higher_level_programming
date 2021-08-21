#!/usr/bin/python3
"""
Write a Python script that takes in a URL,
sends a request to the URL and displays
the body of the response (decoded in utf-8).
"""

from urllib.request import urlopen, Request
from urllib.error import URLError
from sys import argv

if __name__ == "__main__":
    req = Request(url=argv[1])
    try:
        with urlopen(req) as response:
            html = str(response.read())
            print(html[2:-1])
    except URLError as e:
        print("Error code: {}".format(e.code))
