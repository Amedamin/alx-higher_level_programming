#!/usr/bin/python3
"""Python script that takes in a URL"""
import sys
import urllib.request
import urllib.error


if __name__ == "__main__":
    U = sys.argv[1]
    R = urllib.request.Request(U)

    try:
        with urllib.request.urlopen(R) as res:
            X = res.read().decode('utf-8')
            print(X)
    except urllib.error.HTTPError as E:
        print(f"Error code: {E.code}")
