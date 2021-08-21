#!/usr/bin/python3
"""
Write a Python script that fetches https://intranet.hbtn.io/status
"""

import requests

actions = [("type", lambda r: type(r.text)), ("content", lambda r: r.text)]

req = requests.get("https://intranet.hbtn.io/status")
print("Body response:")
[print("\t- {}: {}".format(header, fun(req))) for header, fun in actions]
