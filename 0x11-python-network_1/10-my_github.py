#!/usr/bin/python3
"""
Uses the GitHub API with Basic Authentication"""
import requests
from sys import argv


if __name__ == "__main__":
    U = argv[1]
    PASSW = argv[2]

    URL = 'https://api.github.com/user'
    r = requests.get(URL, auth=(U, PASSW))

    if r.status_code == 200:
        user_in = r.json()
        user_id = user_in.get('id')
        print(user_id)
    else:
        print("None")
