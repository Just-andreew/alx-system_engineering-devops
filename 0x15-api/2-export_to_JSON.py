#!/usr/bin/python3
"""Gather data about completed tasks for specific user, and
export data as json file"""

import json
import requests
import sys

if __name__ == "__main__":

    if sys.argv[1].isdigit():

        user_id = sys.argv[1]
        employee = requests.get('https://jsonplaceholder.typicode.com/users',
                                params={'id':  user_id})
        tasks = requests.get('https://jsonplaceholder.typicode.com/todos',
                             params={'userId':  user_id})

        user_name = employee.json()[0].get('username')

    data = {}
    list_tasks = []
    for task in tasks.json():
        new_task = {}
        new_task['task'] = task.get('title')
        new_task['completed'] = task.get('completed')
        new_task['username'] = user_name
        list_tasks.append(new_task)
    data['{}'.format(user_id)] = list_tasks

    with open('{}.json'.format(user_id), 'w') as json_file:
        json.dump(data, json_file)
