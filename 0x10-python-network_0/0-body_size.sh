#!/bin/bash
# Displays the size of the body of the http response
curl -s --head "$1" | grep "Content-Length" | awk '{print $2}'
