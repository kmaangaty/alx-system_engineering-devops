#!/usr/bin/python3
"""
   Queries the Reddit API and returns the number of subscribers for a given subreddit.

   Args:
       subreddit (str): The name of the subreddit to query.

   Returns:
       int: The number of subscribers of the subreddit. Returns 0 if the subreddit is invalid
       or if there was an error querying the API.
"""
import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        int: The number of subscribers of the subreddit. Returns 0 if the subreddit is invalid
        or if there was an error querying the API.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Custom User Agent'}  # Set a custom User-Agent
    response = requests.get(url, headers=headers)

    # Check if the response is successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        # Extract and return the number of subscribers
        return data['data']['subscribers']
    elif response.status_code == 404:  # Subreddit not found
        return 0
    else:
        print(f"Error: {response.status_code}")
        return 0


# Test the function
if __name__ == "__main__":
    subreddit = input("Enter subreddit name: ")
    print(number_of_subscribers(subreddit))
