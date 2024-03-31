#!/usr/bin/python3
"""
Sends a POST request with an email parameter
"""
from urllib import request, error
import sys


if __name__ == "__main__":
    U = argv[1]
    email = argv[2]

    D = urllib.parse.urlencode({'email': email}).encode('utf-8')
    R = request.Request(U, D)

    with request.urlopen(R) as r:
        B = r.read().decode('utf-8')
        print(B)
