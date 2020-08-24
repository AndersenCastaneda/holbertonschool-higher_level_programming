#!/usr/bin/python3
"""Takes a URL and an email, sends a POST request to the
passed URL with the email as a parameter, and displays
the body of the response(decoded in utf - 8) """


if __name__ == "__main__":
    from urllib import request, parse
    import sys

    url = sys.argv[1]
    email = parse.urlencode(
        {'email': '{}'.format(sys.argv[2])}).encode("utf-8")
    with request.urlopen(url, email) as response:
        print(response.read().decode('utf-8'))
