#!/usr/bin/python3
"""takes your Github credentials (username and password)
and uses the Github API to display your id"""


if __name__ == "__main__":
    import requests
    from sys import argv

    url = 'https://api.github.com/repos/{}/{}/commits'.format(argv[2], argv[1])
    request = requests.get(url)

    commits = request.json()
    for commit in commits[:10]:
        sha = commit.get('sha')
        author = commit.get('commit').get('author').get('name')
        print('{}: {}'.format(sha, author))
