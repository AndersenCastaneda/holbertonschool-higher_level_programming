#!/bin/bash
# Sends a JSON POST request to a URL and displays the response
curl -s "$1" -H "Content-Type: application/json" -d @"$2"
