#!/usr/bin/python3
"""Gather data about completed tasks for specific user,
 and export data to CSV format"""

import csv
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

        with open('{}.csv'.format(user_id), 'w', newline='') as o:
            f = ["USER_ID", "USERNAME\
", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
            writer = csv.DictWriter(o, fieldnames=f, quoting=csv.QUOTE_ALL)
            for task in tasks.json():
                result = {"USER_ID": user_id, "USERNAME\
": user_name, "TASK_TITLE": task.get('title')}
                if task.get('completed'):
                    result["TASK_COMPLETED_STATUS"] = True
                    writer.writerow(result)
                else:
                    result["TASK_COMPLETED_STATUS"] = False
                    writer.writerow(result)
