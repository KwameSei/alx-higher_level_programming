#!/usr/bin/env bash
# Script that takes in url and displays the size of the body
curl -s $1 | wc -c
