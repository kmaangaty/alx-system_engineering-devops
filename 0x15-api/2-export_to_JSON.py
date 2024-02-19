#!/usr/bin/python3
"""
Return information for a given employee about his/her TODO list progress
"""
if __name__ == "__main__":
    import json
    import requests
    import sys

    at = 0
    dt = 0
    cl = []
    us_rls = f'https://jsonplaceholder.typicode.com/users/{sys.argv[1]}'
    tds = 'https://jsonplaceholder.typicode.com/todos'
    rt = requests.get(us_rls)
    ro = requests.get(tds)
    n = rt.json().get('name')
    un = rt.json().get('username')
    tdl = ro.json()
    with open(sys.argv[1] + '.json', 'w+') as file:
        json.dump({sys.argv[1]: [{
            "task": todo.get("title"),
            "completed": todo.get("completed"),
            "username": un} for todo in tdl]}, file)
