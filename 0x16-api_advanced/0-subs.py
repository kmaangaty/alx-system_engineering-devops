#!/usr/bin/python3
"""
    function that queries the Reddit API and returns
    the number of subscribers (not active users, total subscribers)
    for a given subreddit. If an invalid subreddit is given,
    the function should return 0.
"""
import requests


def number_of_subscribers(subreddit):
    """
        function that queries the Reddit API and returns
        the number of subscribers (not active users, total subscribers)
        for a given subreddit. If an invalid subreddit is given,
        the function should return 0.
    """
    rbt = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    hds = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    rp = requests.get(rbt, headers=hds, allow_redirects=False)
    if rp.status_code == 404:
        return 0
    return rp.json().get("data").get("subscribers")
