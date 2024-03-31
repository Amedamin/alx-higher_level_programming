#!/usr/bin/python3
"""script that fetches"""
import urllib.request


def main():
    U = 'https://alx-intranet.hbtn.io/status'

    R = urllib.request.Request(U)

    with urllib.request.urlopen(R) as r:
        C = r.read()
        print("Body response:")
        print("\t- type:", type(C))
        print("\t- content:", C)
        print("\t- utf8 content:", C.decode('utf-8'))


if __name__ == "__main__":
    main()
