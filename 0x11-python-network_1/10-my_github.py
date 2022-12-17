#!/usr/bin/python3
"""
    script that takes user GitHub credentials (username and password)
    and uses the GitHub API to display user id
"""
import requests as req
from sys import argv
from requests.auth import HTTPBasicAuth

if __name__ == '__main__':
    auth = HTTPBasicAuth(argv[1], argv[2])
    result = req.get("https://api.github.com/user", auth=auth)
    print(result.json().get("id"))
