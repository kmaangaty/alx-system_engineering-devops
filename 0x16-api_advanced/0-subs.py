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
        int: The total number of subscribers for the subreddit.
        Returns None if the subreddit is not found or if there is an error.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Custom User Agent'}  # Set a custom User-Agent
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check if the response is successful (status code 200)
    if response.status_code == 200:
        data = response.json()
        return data['data']['subscribers']
    elif response.status_code == 404:  # Subreddit not found
        return None
    else:
        print(f"Error: {response.status_code}")
        return None


# Test the function
if __name__ == "__main__":
    subreddit = input("Enter subreddit name: ")
    subscribers = number_of_subscribers(subreddit)
    if subscribers is None:
        print("Subreddit not found or error occurred.")
    else:
        print(subscribers)