#!/usr/bin/python3
"""
    # Script that fetches https://alx-intranet.hbtn.io/status
    #status
"""
import urllib.request as req

if __name__ == '__main__':
    url = req.Request('https://alx-intranet.hbtn.io/status')
    with req.urlopen(url) as res:
        html = res.read()

        print("Body response:")
        print("\t - type: {}".format(type(html)))
        print("\t - content: {}".format(html))
        print("\t - utf8 content: {}".format(html.decode('utf8')))
