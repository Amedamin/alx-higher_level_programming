#!/usr/bin/python3
"""Python script that takes in a URL"""
from urllib import request, error
import sys


if __name__ == "__main__":
    U = argv[1]
    R = request.Request(U)

    try:
        with request.urlopen(R) as res:
            X = res.read().decode('utf-8')
            print(X)
    except error.HTTPError as E:
        print(f"Error code: {E.code}")
