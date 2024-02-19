#!/usr/bin/python3
"""
Export data in JSON format
Records all tasks from all employees
"""

if __name__ == "__main__":
    # Import necessary libraries
    import json
    import requests

    # Define the filename for the JSON output
    fn = 'todo_all_employees.json'

    # URLs to fetch TODO list data for all users and user information
    us_rls = 'https://jsonplaceholder.typicode.com/users'
    tds = 'https://jsonplaceholder.typicode.com/todos'

    # Send requests to the URLs to get data
    rt = requests.get(tds)
    ro = requests.get(us_rls)

    # Parse the JSON responses
    tdss = rt.json()
    uss = ro.json()

    # Dictionary to store tasks for all employees
    tae = {}

    # Iterate through each user
    for u in uss:
        # List to store tasks for the current user
        task_list = []

        # Iterate through all tasks
        for t in tdss:
            # Check if the task belongs to the current user
            if t.get("userId") == u.get("id"):
                # Create a dictionary for the task
                task_obj = {
                    "username": u.get("username"),
                    "task": t.get("title"),
                    "completed": t.get("completed")
                }

                # Append the task information to the list
                task_list.append(task_obj)

        # Add the list of tasks for the current user to the dictionary
        tae[u.get("id")] = task_list

    # Write the JSON data to a file
    with open(fn, 'w+') as file:
        json.dump(tae, file)
