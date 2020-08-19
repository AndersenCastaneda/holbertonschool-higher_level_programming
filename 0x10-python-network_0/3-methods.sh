#!/bin/bash
# Displays all HTTP methods the server will accept
curl -s --head "$1" | grep "Allow" | sed "s/Allow: //g"
