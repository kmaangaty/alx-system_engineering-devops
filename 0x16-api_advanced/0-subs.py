#!/usr/bin/python3
"""
    recursive function that queries the Reddit API and
    returns a list containing the titles of all hot articles
    for a given subreddit. If no results are found
    for the given subreddit, the function should return None.
"""
import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = "https://www.reddit.com/r/programming/about.json"
    headers = {'User-Agent': 'Mozilla/10.0/API'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0
    try:
        results = response.json().get("data")
        return results.get("subscribers")
    except Exception as e:
        print("Error decoding JSON response:", e)
        print("Response content:", response.content)
        return None
