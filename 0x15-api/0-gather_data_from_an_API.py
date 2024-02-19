#!/usr/bin/python3
"""
This script retrieves and displays information about
 an employee's TODO list progress.
It takes an employee ID as a command-line argument
 and fetches data from a public REST API.
"""


if __name__ == "__main__":
    import requests
    import sys

    # Initialize variables for completed tasks (dt) and total tasks (at)
    dt = 0
    at = 0

    # URL to fetch user information based on the provided employee ID
    user_url = f'https://jsonplaceholder.typicode.com/users/{sys.argv[1]}'

    # URL to fetch TODO list data for all users
    todos_url = 'https://jsonplaceholder.typicode.com/todos'

    # Send requests to the URLs to get data
    response_todos = requests.get(todos_url)
    response_user = requests.get(user_url)

    # Parse the JSON responses
    todos_data = response_todos.json()
    user_data = response_user.json()

    # Get the name of the employee
    employee_name = user_data.get('name')

    # Iterate through the TODO list data
    for todo in todos_data:
        # Count all tasks for the specified user
        if todo.get('userId') == int(sys.argv[1]):
            at += 1
        # Count completed tasks for the specified user
        if todo.get('userId') == int(sys.argv[1]) and todo.get('completed'):
            dt += 1

    # Display employee TODO list progress
    print(f"Employee {employee_name} is done with tasks({dt}/{at}):")

    # Display titles of completed tasks with proper indentation
    for todo in todos_data:
        if todo.get('userId') == int(sys.argv[1]) and todo.get('completed'):
            print(f"	 {todo.get('title')}")
