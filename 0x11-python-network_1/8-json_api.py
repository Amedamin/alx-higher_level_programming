#!/usr/bin/python3
"""
Sends a POST request to http://0.0.0.0:5000/search_user
with a letter as a parameter.
Displays the id and name from the JSON response"""
import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) < 2:
        q = ""
    else:
        q = argv[1]

    U = 'http://0.0.0.0:5000/search_user'
    payload = {'q': q}

    r = requests.post(U, data=payload)

    try:
        json_r = r.json()
        if json_r:
            print("[{}] {}".format(json_r['id'], json_r['name']))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
