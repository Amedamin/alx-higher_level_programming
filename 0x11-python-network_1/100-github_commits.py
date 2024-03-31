#!/usr/bin/python3
"""Python script that sends a request to the URL and
"""
import sys
import requests


if __name__ == "__main__":
    u = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1])

    E = requests.get(u)
