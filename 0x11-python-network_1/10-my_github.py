#!/usr/bin/python3
"""Sript that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id"""


import requests
import sys


if __name__ == '__main__':
    username = sys.argv[1]
    access_token = sys.argv[2]
    url = 'https://api.github.com/user'
    headers = {
        'Authorization': f'Basic {username}:{access_token}'
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        user_info = response.json()
        print(user_info['id'])
    else:
        print("None")
