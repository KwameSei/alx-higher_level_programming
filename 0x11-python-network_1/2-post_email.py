#!/usr/bin/python3
"""
    script that takes in a URL and an email,
    sends a POST request to the passed URL with the email
    as a parameter, and displays the body of the response
    (decoded in utf-8)
"""
import urllib.request as req
import urllib.parse as u_parse
from sys import argv


if __name__ == '__main__':
    url = argv[1]
    value = {'email': argv[2]}
    data = u_parse.urlencode(value)
    data = data.encode('ascii')     # encode values

    request = req.Request(url, data)
    with req.urlopen(request) as res:
        print(res.read().decode('utf-8'))
