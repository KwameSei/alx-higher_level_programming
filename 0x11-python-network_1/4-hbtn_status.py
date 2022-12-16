#!/usr/bin/python3
"""
    Script that fetches https://alx-intranet.hbtn.io/status
    status
"""
import requests as req


if __name__ == '__main__':
    url = req.get('https://alx-intranet.hbtn.io/status')

    print("Body response:")
    print("\t- type: {}".format(type(url.text)))
    print("\t- content: {}".format(url.text))
