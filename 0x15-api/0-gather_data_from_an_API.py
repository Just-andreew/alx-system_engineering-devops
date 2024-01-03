#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""

import sys
import requests

if __name__ == "__main__":
    if len(sys.argv) < 2 or not sys.argv[1].isdigit():
        print("Usage: python script.py <user_id>")
        sys.exit(1)

    user_id = sys.argv[1]
    employee = requests.get('https://jsonplaceholder.typicode.com/users', params={'id': user_id})
    tasks = requests.get('https://jsonplaceholder.typicode.com/todos', params={'userId': user_id})

    if employee.status_code != 200 or tasks.status_code != 200:
        print("Error fetching data. Please check the user ID.")
        sys.exit(1)

    user_name = employee.json()[0].get('name')
    total_tasks = len(tasks.json())
    done_tasks = 0

    # Count done tasks
    for task in tasks.json():
        if task.get('completed'):
            done_tasks += 1

    print("Employee {} is done with tasks({}/{}):".format(user_name, done_tasks, total_tasks))
    for task in tasks.json():
        if task.get('completed'):
            print("\t{}".format(task.get('title')))
