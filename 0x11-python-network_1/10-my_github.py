#!/usr/bin/python3
"""
    script that takes user GitHub credentials (username and password)
    and uses the GitHub API to display user id
"""
import requests as req
from sys import argv
from request.auth import HTTPBasicAuth

if __name__ == '__main__':
    auth = HTTPBasicAuth(argv[1], argv[2])
    url = "https://api.github.com/user"
    result = req.get(url, auth=auth)
    print(result.json().get("id"))
