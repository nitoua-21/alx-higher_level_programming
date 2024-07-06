#!/usr/bin/python3
"""Sript that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id"""


import requests
import sys


if __name__ == '__main__':
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    params = {
        'per_page': 10,
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        commits = response.json()
        for commit in commits:
            sha = commit['sha']
            author_name = commit['commit']['author']['name']
            print(f"{sha}: {author_name}")
    else:
        print(f"Error fetching commits: {response.status_code}")
