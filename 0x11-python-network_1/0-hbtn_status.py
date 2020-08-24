#!/usr/bin/python3
"""Fetches https://intranet.hbtn.io/status"""

if __name__ == "__main__":
    import urllib.request

    intranet = 'https://intranet.hbtn.io/status'
    with urllib.request.urlopen(intranet) as response:
        resp = response.read()
        print("Body response:")
        print("\t- type {}".format(type(resp)))
        print("\t- content: {}".format(resp))
        print("\t- utf8 content: {}".format(resp.decode("utf-8")))
