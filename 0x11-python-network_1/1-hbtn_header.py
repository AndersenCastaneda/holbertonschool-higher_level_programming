#!/usr/bin/python3
"""Takes a URL, sends a request to the URL and
displays the value of the X-Request-Id variable
found in the header of the response"""


if __name__ == "__main__":
    import urllib.request as request
    import sys

    with request.urlopen(sys.argv[1]) as response:
        print(response.headers.get('X-Request-Id'))
