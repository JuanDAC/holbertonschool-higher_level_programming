#!/usr/bin/env bash
# 
curl -sI "$1" | grep Allow | cut --delimiter=" " --fields=2-
