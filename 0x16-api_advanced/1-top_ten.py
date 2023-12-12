#!/usr/bin/python3
"""Function to print hot posts on Reddit subreddit."""
import requests


def top_ten(subreddit):
    """Print the 10 hottest posts on a given subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"

    headers = {
        'User-Agent': 'Esraa1993'
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        for post in posts:
            title = post['data']['title']
            print(title)
    if response.status_code == 404:
        print("None")
