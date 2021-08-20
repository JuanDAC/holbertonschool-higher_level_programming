#!/usr/bin/env bash
# Bash script that sends a request to a URL passed as an argument
curl -so /dev/null -sw "%{http_code}" "$1"
