#!/usr/bin/python3
"""
export data in JSON format
Records all tasks from all employees
"""
if __name__ == "__main__":
    import json
    import requests

    fn = 'todo_all_employees.json'
    us_rls = 'https://jsonplaceholder.typicode.com/users'
    tds = 'https://jsonplaceholder.typicode.com/todos'
    rt = requests.get(tds)
    ro = requests.get(us_rls)
    tdss = rt.json()
    uss = ro.json()
    tae = {}

    for u in uss:
        list = []
        for t in tdss:
            if t.get("userId") == u.get("id"):
                obj = {"username": u.get("username"),
                           "task": t.get("title"),
                           "completed": t.get("completed")}
                list.append(obj)
        tae[u.get("id")] = list
    with open(fn, 'w+') as file:
        json.dump(tae, file)
