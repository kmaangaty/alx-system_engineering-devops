#!/usr/bin/python3
"""
    recursive function that queries the Reddit API and
    returns a list containing the titles of all hot articles
    for a given subreddit. If no results are found
    for the given subreddit, the function should return None.
"""
import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The total number of subscribers for the subreddit. Returns 0 if the subreddit is invalid.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'Custom User Agent'}

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        return data['data']['subscribers']
    else:
        return response


# Test the function
if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subscribers = number_of_subscribers(sys.argv[1])
        print(subscribers)