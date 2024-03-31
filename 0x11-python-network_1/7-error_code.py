#!/usr/bin/python3
"""
Sends a request to the given URL.
"""
import requests
import sys


if __name__ == "__main__":
    U = sys.argv[1]
    r = requests.get(U)

    if r.status_code >= 400:
        print(f"Error code: {r.status_code}")
    else:
        print(r.text)
