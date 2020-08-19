#!/bin/bash
# Sends a POST request and displays the body
curl -s -X POST "$1" -d "email=hr@holbertonschool.com" -d "subject=I will always be here for PLD"
