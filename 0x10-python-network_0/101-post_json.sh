#!/usr/bin/env bash
# Script that sends a POST request with some information
curl -sH "Content-Type: application/json" -X POST -d @"$2" "$1"
