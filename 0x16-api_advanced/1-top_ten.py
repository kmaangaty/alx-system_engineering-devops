#!/usr/bin/python3
"""function that queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit."""
import requests


def top_ten(subreddit):
    """function that queries the Reddit API and prints the titles
    of the first 10 hot posts listed for a given subreddit."""
    rpt = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    hds = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    pms = {
        "limit": 10
    }
    rp = requests.get(rpt, headers=hds, params=pms,
                      allow_redirects=False)
    if rp.status_code == 404:
        print("None")
        return
    data = rp.json().get("data")
    [print(c.get("data").get("title")) for c in data.get("children")]
