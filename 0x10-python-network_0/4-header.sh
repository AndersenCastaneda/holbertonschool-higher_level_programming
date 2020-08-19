#!/bin/bash
# Sends a GET request to the URL and a Custom Header variable
curl -s --header "X-HolbertonSchool-User-Id: 98" "$1"
