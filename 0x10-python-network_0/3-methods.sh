#!/usr/bin/env bash
# Script that takes in a URL and displays all HTTP methods
curl -sI "$1" | grep -i 'allow' | cut -d " " -f2-
