#!/usr/bin/python3
"""
    sending request to the URL and displaying the body
    of the response (decoded in utf-8).
"""
from urllib import request as req, error
from sys import argv


if __name__ == '__main__':

    url = argv[1]
    try:
        with req.urlopen(url) as res:
            print(res.read().decode('utf-8'))
    except error.HTTPError as er:
        print('Error code:', er.code)
