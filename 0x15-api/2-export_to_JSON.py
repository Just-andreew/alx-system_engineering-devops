#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to JSON format."""
import json
import requests
import sys

def get_employee_todo_data_and_export_to_json(employee_id):
    """Retrieves TODO data for the given employee ID and exports it to a JSON file.

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

        # Prepare JSON data
        json_data = {
            employee_id: [
                {
                    "task": todo["title"],
                    "completed": todo["completed"],
                    "username": employee_data["name"]
                } for todo in todos_data
            ]
        }

        # Export to JSON file
        with open(f"{employee_id}.json", "w") as jsonfile:
            json.dump(json_data, jsonfile, indent=4)  # Add indentation for readability

        print(f"Employee TODO data exported to {employee_id}.json")

    except Exception as e:
        print(f"Error fetching or processing API data: {e}")

if __name__ == "__main__":
    employee_id = int(input("Enter employee ID: "))
    get_employee_todo_data_and_export_to_json(employee_id)
