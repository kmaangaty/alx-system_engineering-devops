#!/usr/bin/python3
"""
Return information for a given employee about his/her TODO list progress
"""

if __name__ == "__main__":
    # Import necessary libraries
    import json
    import requests
    import sys

    # Initialize variables for completed tasks (dt), all tasks (at), and a list to store data for JSON
    at = 0
    dt = 0
    cl = []

    # URL to fetch user information based on provided employee ID
    us_rls = f'https://jsonplaceholder.typicode.com/users/{sys.argv[1]}'

    # URL to fetch TODO list data for all users
    tds = 'https://jsonplaceholder.typicode.com/todos'

    # Send requests to the URLs to get data
    rt = requests.get(us_rls)
    ro = requests.get(tds)

    # Parse the JSON responses
    n = rt.json().get('name')
    un = rt.json().get('username')
    tdl = ro.json()

    # Iterate through the TODO list data
    for todo in tdl:
        # Check if the task belongs to the specified user
        if todo.get('userId') == int(sys.argv[1]):
            # Count all tasks for the specified user
            at += 1

            # Count completed tasks for the specified user
            if todo.get('completed'):
                dt += 1

            # Append task information to the list
            cl.append({
                "task": todo.get("title"),
                "completed": todo.get("completed"),
                "username": un
            })

    # Write JSON data to a file
    with open(sys.argv[1] + '.json', 'w+') as file:
        json.dump({sys.argv[1]: cl}, file)
