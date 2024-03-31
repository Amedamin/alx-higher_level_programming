#!/usr/bin/python3
"""
Sends a POST request with email parameter to the given URL"""
import requests
import sys


if __name__ == "__main__":
    U = sys.argv[1]
    email = sys.argv[2]

    p = {'email': email}
    r = requests.post(U, data=p)

    print(r.text)
