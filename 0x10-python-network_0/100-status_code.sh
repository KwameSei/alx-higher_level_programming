#!/bin/bash
# Script that sends a request and displays only status code
curl -sw "%{http_code}" -o /dev/null "$1"
