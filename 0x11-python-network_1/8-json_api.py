#!/usr/bin/python3
"""Takes a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter"""


if __name__ == "__main__":
    import requests
    import sys

    q = sys.argv[1] if len(sys.argv) == 2 else ""
    url = 'http://0.0.0.0:5000/search_user'
    request = requests.post(url, data={'q': q})
    try:
        dt = request.json()
        if len(dt) > 0:
            print('[{}] {}'.format(dt.get('id'), dt.get('name')))
        else:
            print('No result')
    except ValueError:
        print('Not a valid JSON')
