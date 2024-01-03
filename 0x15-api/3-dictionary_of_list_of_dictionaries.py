#!/usr/bin/python3
"""Exports to-do list information of all employees to JSON format."""
import json
import requests

def get_all_employees_todo_data_and_export_to_json():
    """Retrieves TODO data for all employees and exports it to a JSON file.
    """

    try:
        # Fetch all employee IDs
        employees_url = "https://jsonplaceholder.typicode.com/users"
        employees_response = requests.get(employees_url)
        employees_data = employees_response.json()
        employee_ids = [employee["id"] for employee in employees_data]

        # Collect TODO data for each employee
        all_employee_data = {}
        for employee_id in employee_ids:
            employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
            employee_response = requests.get(employee_url)
            employee_data = employee_response.json()

            todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
            todos_response = requests.get(todos_url)
            todos_data = todos_response.json()

            all_employee_data[employee_id] = [
                {
                    "username": employee_data["username"],
                    "task": todo["title"],
                    "completed": todo["completed"]
                } for todo in todos_data
            ]

        # Export to JSON file
        with open("todo_all_employees.json", "w") as jsonfile:
            json.dump(all_employee_data, jsonfile, indent=4)  # Add indentation for readability

        print("All employee TODO data exported to todo_all_employees.json")

    except Exception as e:
        print(f"Error fetching or processing API data: {e}")

if __name__ == "__main__":
    get_all_employees_todo_data_and_export_to_json()
