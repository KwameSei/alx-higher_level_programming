#!/bin/bash
# Script that sends a JSON POST request and displays the body
curl -sL -X POST -d "@$2" -H "Content-Type: application/json" "$1"
