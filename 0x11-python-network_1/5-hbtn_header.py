#!/usr/bin/python3
"""
Displays the value of the X-Request-Id variable
found in the header of the response.
"""
import sys
import requests


if __name__ == "__main__":
    U = sys.argv[1]
    r = requests.get(U)

    h = r.headers.get("X-Request-Id")
    print(h)
