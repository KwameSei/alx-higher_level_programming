#!/bin/bash
# Making a request to the server that responds "You got me"
curl -sL -d PUT "user_id=98" -H "Origin:HolbertonSchool" "0.0.0.0:5000/catch_me"
