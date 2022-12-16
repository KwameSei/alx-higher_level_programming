#!/usr/bin/python3
"""
    script that takes in a URL, sends a request to the URL 
    and displays the value of the X-Request-Id variable 
    found in the header of the response.
"""


import requests as req
from sys import argv

if __name__ == '__main__':
    url = argv[1]
    
    result = req.get(url)
    print(result.headers.get('X-Request-Id'))
