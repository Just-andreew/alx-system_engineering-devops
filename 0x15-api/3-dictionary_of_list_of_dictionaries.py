#!/usr/bin/python3
"""Gather data about completed tasks for all user, and
export data as json file"""

import json
import requests

if __name__ == "__main__":

    employee = requests.get('https://jsonplaceholder.typicode.com/users')
    tasks = requests.get('https://jsonplaceholder.typicode.com/todos')

    data = {}
    for user in employee.json():
        list_tasks = []
        for task in tasks.json():
            new_task = {}
            if task.get('userId') == user.get('id'):
                new_task['task'] = task.get('title')
                new_task['completed'] = task.get('completed')
                new_task['username'] = user.get('username')
                list_tasks.append(new_task)
        data['{}'.format(user.get('id'))] = list_tasks

    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(data, json_file)
