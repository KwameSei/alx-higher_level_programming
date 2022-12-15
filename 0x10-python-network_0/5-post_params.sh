#!/bin/bash
# Script that sends in a URL request and displays the body
curl -s POST -d "$1" "email=test@gmail.com&subject=I will always be here for PLD"
