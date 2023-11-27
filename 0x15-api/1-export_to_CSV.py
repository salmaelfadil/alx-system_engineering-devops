#!/usr/bin/python3
"""
Retuns information about an employee's TODO
list given their ID using REST API
"""
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()

    completed = []
    for i in todos:
        if i.get("completed") is True:
            completed.append(i.get("title"))

    with open("{}.csv".format(user_id), "w", newline="") as csvfile:
        w = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for i in todos:
            w.writerow(user_id, username, 
                    i.get("completed"), i.get("title")
