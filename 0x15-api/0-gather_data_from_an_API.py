#!/usr/bin/python3
"""
This script retrieves information about an employee's TODO list progress
using a REST API. It accepts an employee ID as a parameter and displays
the progress in a specific format.

Requirements:
- Uses the requests module
- Accepts an integer as a parameter (employee ID)
- Displays information in the specified format
"""

import requests
import sys


def get_employee_data(employee_id):
    """
    Fetches employee data and TODO list from a REST API
    and displays the progress in the specified format.

    :param employee_id: Integer, the ID of the employee
    """
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos?userId={employee_id}"

    # Fetch user data
    user_response = requests.get(user_url)
    user_data = user_response.json()
    employee_name = user_data.get("name")

    # Fetch TODO list data
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Calculate TODO progress
    total_tasks = len(todos_data)
    completed_tasks = sum(task['completed'] for task in todos_data)

    # Display employee TODO list progress
    print(f"Employee {employee_name}"
          f" is done with tasks({completed_tasks}/{total_tasks}):")

    # Display titles of completed tasks with 1 tabulation and 1 space before the TASK_TITLE
    for task in todos_data:
        if task['completed']:
            print(f"\t {task['title']}")


if __name__ == "__main__":
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Error: Employee ID must be an integer.")
        sys.exit(1)

    # Retrieve and display employee TODO list progress
    get_employee_data(employee_id)
