#!/usr/bin/python3
# Python script that takes in a URL and prints its header X-Request-Id

from urllib.request import urlopen
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    with urlopen(url) as response:
        headers_like_dict = dict(response.getheaders());
        print(headers_like_dict['X-Request-Id'])
