#!/usr/bin/bash
# Bash script that takes in a URL and displays all HTTP
curl -sI "$1" | grep Allow | cut --delimiter=" " -f 2-
