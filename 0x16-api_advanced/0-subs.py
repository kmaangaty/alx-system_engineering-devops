#!/usr/bin/python3
import requests


def number_of_subscribers(subreddit):
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
