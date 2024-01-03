#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to CSV format."""
import csv
import requests
import sys

def get_employee_todo_data_and_export_to_csv(employee_id):
    """Retrieves TODO data for the given employee ID and exports it to a CSV file.

    Args:
        employee_id (int): The ID of the employee to retrieve information for.

    Raises:
        Exception: If an error occurs while fetching or processing the API data.
    """

    try:
        # Fetch employee and todo data
        employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
        employee_response = requests.get(employee_url)
        employee_data = employee_response.json()

        todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
        todos_response = requests.get(todos_url)
        todos_data = todos_response.json()

        # Prepare CSV data
        csv_data = [
            ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
        ]
        for todo in todos_data:
            csv_data.append([
                employee_id,
                employee_data["name"],
                "Completed" if todo["completed"] else "Incomplete",
                todo["title"]
            ])

        # Export to CSV file
        with open(f"{employee_id}.csv", "w", newline="") as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerows(csv_data)

        print(f"Employee TODO data exported to {employee_id}.csv")

    except Exception as e:
        print(f"Error fetching or processing API data: {e}")

if __name__ == "__main__":
    employee_id = int(input("Enter employee ID: "))
    get_employee_todo_data_and_export_to_csv(employee_id)
