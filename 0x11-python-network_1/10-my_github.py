#!/usr/bin/python3
"""Sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)"""


import requests
import sys


if __name__ == '__main__':
    username = sys.argv[1]
    access_token = sys.argv[2]
    url = f"https://api.github.com/user"
    headers = {
        'Authorization': f'Basic {username}:{access_token}'
    }

    response = requests.post(url, headers=headers)
    if response.status_code == 200:
        user_info = response.json()
        print(user_info['id'])
    else:
        print("None")
