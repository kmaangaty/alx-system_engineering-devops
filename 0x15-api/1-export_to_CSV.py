#!/usr/bin/python3
"""
This script retrieves information about an employee's TODO list progress
using a REST API. It accepts an employee ID as a parameter and displays
the progress in a specific format.
 Additionally, it exports the data to a CSV file.

Requirements:
- Uses the requests module
- Accepts an integer as a parameter (employee ID)
- Displays information in the specified format
- Exports data to CSV file in the format:
 "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
"""

import csv
import requests
import sys


if __name__ == "__main__":
    uid = sys.argv[1]
    link = "https://jsonplaceholder.typicode.com/"
    tds = requests.get(link + "todos", params={"userId": uid}).json()
    us = requests.get(link + "users/{}".format(uid)).json()
    un = us.get("username")

    with open("{}.csv".format(uid), "w", newline="") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [uid, un, t.get("completed"), t.get("title")]
         ) for t in tds]