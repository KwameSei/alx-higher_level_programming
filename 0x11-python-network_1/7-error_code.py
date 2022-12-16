#!/usr/bin/python3
"""
    sending request to the URL and displaying the body
    of the response.
"""
import requests as req
from sys import argv


if __name__ == '__main__':

    url = argv[1]

    result = req.get(url)

    if result.status_code >= 400:
        print('Error code: {}'.format(result.status_code)
    else:
        print(result.text)
