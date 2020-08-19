#!/bin/bash
# Request to 0.0.0.0:5000/catch_me that causes the server to respond with a message containing You got me!
curl -s -X PUT --location 0.0.0.0:5000/catch_me -d "user_id=98" -H "origin: HolbertonSchool"
