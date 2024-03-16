#!/usr/bin/python3
"""
    recursive function that queries the Reddit API and
    returns a list containing the titles of all hot articles
    for a given subreddit. If no results are found
    for the given subreddit, the function should return None.
"""
import requests
import time


def number_of_subscribers(subreddit):
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        'User-Agent': 'MyRedditBot/1.0 by RedditUser123'
    }

    retries = 3
    for attempt in range(retries):
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        elif response.status_code == 404:
            return None
        elif response.status_code == 403:
            print("403 Forbidden: Rate limit exceeded or access denied.")
            if attempt < retries - 1:
                print("Retrying after a short delay...")
                time.sleep(5)  # Wait for 5 seconds before retrying
            else:
                print("Maximum retries exceeded. Exiting.")
                return None
        else:
            print("Error: {}".format(response.status_code))
            return None


if __name__ == "__main__":
    import sys

    subreddit = sys.argv[1] if len(sys.argv) > 1 else input("Enter subreddit name: ")
    subscribers = number_of_subscribers(subreddit)
    if subscribers is None:
        print("Subreddit not found or error occurred.")
    else:
        print(subscribers)
