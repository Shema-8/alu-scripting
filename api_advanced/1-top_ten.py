#!/usr/bin/python3
"""Get the titles of the first 10 hot posts for a given subreddit using Reddit's JSON API."""

import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts in a given subreddit."""
    headers = {'User-Agent': 'MyAPI/0.0.1'}
    subreddit_url = f"https://reddit.com/r/{subreddit}/hot.json?limit=10"
    response = requests.get(subreddit_url, headers=headers)

    if response.status_code == 200:
        json_data = response.json()
        posts = json_data.get('data', {}).get('children', [])
        for post in posts[:10]:
            print(post.get('data', {}).get('title'))
    else:
        print(None)
       
