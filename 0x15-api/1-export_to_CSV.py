#!/usr/bin/python3
"""
exports to CSV format
"""
import csv
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user_id = sys.argv[1]
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    username = user.get("username")
    todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()

    with open("{}.csv".format(user_id), "w", newline="") as csvfile:
        w = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for i in todos:
            w.writerow([user_id, username,
                        i.get("completed"), i.get("title")])
