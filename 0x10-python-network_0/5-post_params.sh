#!/bin/bash
# Script that sends in a URL request and displays the body
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
