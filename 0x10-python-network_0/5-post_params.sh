#!/bin/bash
# Sends a POST request and displays the response
curl -s "$1" -X POST --data "email=hr@holbertonschool.com" --data "subject=I will always be here for PLD"

