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
    Queries the Reddit API and returns the number
     of subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The total number of subscribers for the subreddit.
        Returns None if the subreddit is not found or if there is an error.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/10.0/API'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check if the response is successful (status code 200)
    if response.status_code == 200:
        data = response.json().get("data")
        return data.get('subscribers')
    elif response.status_code == 404:
        print("Error: {}".format(response.status_code))
    elif response.status_code == 403:
        print("Error: {}".format(response.status_code))
        return 0
    else:
        print("Error: {}".format(response.status_code))
        return 0
