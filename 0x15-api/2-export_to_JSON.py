#!/usr/bin/python3
"""
exports to json file
"""
import json
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user_id = sys.argv[1]
    user = requests.get(url + "users/{}".format(user_id)).json()
    username = user.get("username")
    todos = requests.get(url + "todos", params={"userId": user_id}).json()

    with open("{}.json".format(user_id), "w") as jsonfile:
        for i in todos:
            json.dump({
                user_id: [{
                "task": i.get("title"),
                "completed": i.get("completed"),
                "username": username}]}, jsonfile)
