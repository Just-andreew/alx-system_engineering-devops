import sys
import requests
import csv

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
    completed_tasks = []

    for task in tasks.json():
        if task.get('completed'):
            done_tasks += 1
            completed_tasks.append({
                "USER_ID": user_id,
                "USERNAME": user_name,
                "TASK_COMPLETED_STATUS": "Completed",
                "TASK_TITLE": task.get('title')
            })

    # Export data to CSV
    csv_file_name = "{}.csv".format(user_id)
    with open(csv_file_name, mode='w', newline='') as csv_file:
        fieldnames = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(completed_tasks)

    print("Employee {} is done with tasks({}/{}). CSV file '{}' created.".format(user_name, done_tasks, total_tasks, csv_file_name))
