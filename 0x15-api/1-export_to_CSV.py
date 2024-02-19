#!/usr/bin/python3
"""
This script retrieves information about an employee's TODO list progress
using a REST API. It accepts an employee ID as a parameter and displays
the progress in a specific format. Additionally, it exports the data to a CSV file.

Requirements:
- Uses the requests module
- Accepts an integer as a parameter (employee ID)
- Displays information in the specified format
- Exports data to CSV file in the format: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
"""

import requests
import sys
import csv


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
    print(f"Employee {employee_name} is done with tasks({completed_tasks}/{total_tasks}):")

    # Display titles of completed tasks
    for task in todos_data:
        if task['completed']:
            print(f"\t{task['title']}")
            export_to_csv(employee_id, employee_name, task)


def export_to_csv(employee_id, employee_name, task):
    """
    Exports TODO list data to a CSV file.

    :param employee_id: Integer, the ID of the employee
    :param employee_name: String, the name of the employee
    :param task: Dictionary, the task details
    """
    csv_file_name = f"{employee_id}.csv"

    with open(csv_file_name, mode='a', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        writer.writerow([employee_id, employee_name, str(task['completed']), task['title']])


if __name__ == "__main__":
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Error: Employee ID must be an integer.")
        sys.exit(1)

    # Retrieve and display employee TODO list progress
    get_employee_data(employee_id)
