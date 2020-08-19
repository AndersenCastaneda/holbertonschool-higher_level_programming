#!/bin/bash
# Sends a request to a URL passed as an argument
curl -s -o /dev/null --head -w "%{http_code}" "$1"
