#!/usr/bin/python3
"""takes your Github credentials (username and password)
and uses the Github API to display your id"""


if __name__ == "__main__":
    import requests
    from requests.auth import HTTPBasicAuth
    from sys import argv

    url = 'https://api.github.com/repos/{}/{}/commits'.format(argv[1], argv[2])
    request = requests.get(url)
    count = 0
    for elem in request.json():
        if type(elem) == dict:
            count += 1
            commits = elem.get('commit')
            commit = commits.get('tree').get('sha')
            author = commits.get('author').get('name')
            print('{}: {}'.format(commit, author))
            if count == 10:
                break
