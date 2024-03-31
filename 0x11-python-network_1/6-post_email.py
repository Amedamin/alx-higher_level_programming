#!/usr/bin/python3
"""
Sends a POST request with email parameter to the given URL"""
import requests
from sys import argv


if __name__ == "__main__":
    U = argv[1]
    email = argv[2]

    p = {'email': email}
    r = requests.post(U, data=p)

    print(r.text)
