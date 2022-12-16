#!/usr/bin/python3
"""
    # Script that fetches https://alx-intranet.hbtn.io/status
    #status
"""
import urllib.request as req
from sys import argv

if __name__ == '__main__':
    url = argv[1]
    with req.urlopen(url) as res:
        html = res.read()
        data = dict(res.headers)
        print(data['X-Request-Id'])
