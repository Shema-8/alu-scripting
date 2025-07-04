#!/usr/bin/python3
"""Get the titles of the first 10 hot posts for a given subreddit using Reddit's JSON API."""

import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts from a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "python:subreddit.top10:v1.0 (by /u/your_username)"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        posts = response.json().get("data", {}).get("children", [])
        for post in posts:
            print(post.get("data", {}).get("title"))
    else:
        print(None)
