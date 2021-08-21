#!/usr/bin/python3
# Python script that fetches https://intranet.hbtn.io/status

from urllib.request import urlopen

actions = [
        ("type", lambda html : type(html)),
        ("content", lambda html : html),
        ("utf8 content", lambda html : html.decode()),
]

with urlopen('https://intranet.hbtn.io/status') as response:
    html = response.read()
    print("Body response:")
    [print("\t- {}: {}".format(header, value(html))) for header, value in actions]
