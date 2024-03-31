#!/usr/bin/python3
"""Python script that fetches url"""
import requests


if __name__ == "__main__":
    U = 'https://alx-intranet.hbtn.io/status'
    r = requests.get(U)

    print("Body response:")
    print("\t- type:", type(r.text))
    print("\t- content:", r.text)
