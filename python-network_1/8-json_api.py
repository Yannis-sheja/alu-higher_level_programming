#!/usr/bin/python3
"""Sends a POST request with a letter parameter to the search_user endpoint."""
import sys
import requests

if __name__ == "__main__":
    letter = ""
    if len(sys.argv) > 1:
        letter = sys.argv[1]

    url = "http://0.0.0.0:5000/search_user"
    r = requests.post(url, data={"q": letter})

    if r.text == "":
        print("No result")
    else:
        try:
            j = r.json()
        except ValueError:
            print("Not a valid JSON")
        else:
            if not j:
                print("No result")
            else:
                print("[{}] {}".format(j.get("id"), j.get("name")))
