#!/usr/bin/python3
"""
This script retrieves information about an employee's
 TODO list progress
and exports the data to a JSON file.

Usage:
    python3 script_name.py <employee_id>

Arguments:
    <employee_id>: Integer representing the employee ID.

The script fetches data from the JSONPlaceholder
 API to gather information
about the specified employee's TODO list progress.
 It counts the completed
tasks, displays progress information, and exports
 the data to a JSON file.

Requirements:
- Uses the requests module.
"""

if __name__ == "__main__":
    import json
    import requests
    import sys

    # Initialize variables for completed tasks (dt),
    # all tasks (at), and a list to store data for JSON
    dt = 0
    at = 0
    json_data = {}

    # URL to fetch user information based on provided employee ID
    user_url = (f'https://jsonplaceholder.typicode.com/users/'
                f'{sys.argv[1]}')

    # URL to fetch TODO list data for all users
    todos_url = 'https://jsonplaceholder.typicode.com/todos'

    # Send requests to the URLs to get data
    response_user = requests.get(user_url)
    response_todos = requests.get(todos_url)

    # Parse the JSON responses
    user_data = response_user.json()
    todos_data = response_todos.json()

    # Get the name, username, and employee ID
    employee_name = user_data.get('name')
    username = user_data.get('username')
    employee_id = sys.argv[1]

    # Iterate through the TODO list data
    for todo in todos_data:
        # Check if the task belongs to the specified user
        if todo.get('userId') == int(employee_id):
            # Count all tasks for the specified user
            at += 1

            # Count completed tasks for the specified user
            if todo.get('completed'):
                dt += 1

            # Store task information in the JSON data dictionary
            json_data[employee_id] = [{
                "task": todo.get("title"),
                "completed": todo.get("completed"),
                "username": username
            }]

    # Write JSON data to a file
    with open(f"{employee_id}.json", 'w+') as file:
        json.dump(json_data, file)
