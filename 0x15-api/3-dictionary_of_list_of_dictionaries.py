#!/usr/bin/python3
"""
exports all employee info to json file
"""
import json
import requests


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users").json()

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump({
            u.get("id"): [{
                "task": d.get("title"),
                "completed": d.get("completed"),
                "username": u.get("username")
            } for d in requests.get(url + "todos",
                                    params={"userId": u.get("id")}).json()]
            for u in users}, jsonfile)
