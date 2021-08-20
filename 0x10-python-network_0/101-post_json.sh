#!/usr/bin/env bash
# Script that sends a POST request with any information
curl -sH "Content-Type: application/json" -d @"$2" "$1"
