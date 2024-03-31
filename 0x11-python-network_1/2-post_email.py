#!/usr/bin/python3
"""
Sends a POST request with an email parameter
"""
import urllib.parse
import urllib.request
import sys

if __name__ == "__main__":
    U = sys.argv[1]
    email = sys.argv[2]

    D = urllib.parse.urlencode({'email': email}).encode('utf-8')
    R = urllib.request.Request(U, D)

    with urllib.request.urlopen(R) as r:
        B = r.read().decode('utf-8')
        print(B)
