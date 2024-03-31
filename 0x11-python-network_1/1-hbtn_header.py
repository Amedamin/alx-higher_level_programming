#!/usr/bin/python3
"""
Displays the value of the X-Request-Id variable
"""
import urllib.request
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./1-hbtn_header.py <URL>")
        sys.exit(1)

    U = sys.argv[1]

    with urllib.request.urlopen(U) as r:
        x_r_id = r.headers.get('X-Request-Id')
        print(x_r_id)
