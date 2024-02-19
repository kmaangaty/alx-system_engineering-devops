#!/usr/bin/python3
"""
This script retrieves information about a
 given employee's TODO list progress
and exports the data to a CSV file.
"""

if __name__ == "__main__":
    import csv
    import requests
    import sys

    # Initialize variables for completed tasks (dt), all tasks (at), and a list to store data for CSV
    dt = 0
    at = 0
    csv_data = []

    # URL to fetch user information based on provided employee ID
    user_url = (f'https://jsonplaceholder.typicode.com/users/'
                f'{sys.argv[1]}')

    # URL to fetch TODO list data for all users
    todos_url = 'https://jsonplaceholder.typicode.com/todos'

    # Send requests to the URLs to get data
    response_todos = requests.get(todos_url)
    response_user = requests.get(user_url)

    # Parse the JSON responses
    todos_data = response_todos.json()
    user_data = response_user.json()

    # Get the username and name of the employee
    username = user_data.get('username')
    employee_name = user_data.get('name')

    # Iterate through the TODO list data
    for todo in todos_data:
        # Check if the task belongs to the specified user
        if todo.get('userId') == int(sys.argv[1]):
            # Initialize a list to store task information for CSV
            task_info = []

            # Count all tasks for the specified user
            at += 1

            # Append task information to the list for CSV
            task_info.append(todo.get('userId'))
            task_info.append(username)
            task_info.append(todo.get('completed'))
            task_info.append(todo.get('title'))

            # Append the task list to the CSV data list
            csv_data.append(task_info)

            # Count completed tasks for the specified user
            if todo.get('completed'):
                dt += 1

    # Write CSV data to a file
    with open(f"{sys.argv[1]}.csv", 'w+', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        writer.writerows(csv_data)
