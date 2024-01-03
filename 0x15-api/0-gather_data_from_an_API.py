#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import requests
import sys

def get_employee_todo_progress(employee_id):
   """Retrieves and displays TODO list progress for the given employee ID.

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

       # Extract relevant information
       employee_name = employee_data["name"]
       completed_task_count = len([todo for todo in todos_data if todo["completed"]])
       total_task_count = len(todos_data)
       completed_task_titles = [todo["title"] for todo in todos_data if todo["completed"]]

       # Display progress information
       print(f"Employee {employee_name} is done with tasks ({completed_task_count}/{total_task_count}):")
       for title in completed_task_titles:
           print("\t", title)

   except Exception as e:
       print(f"Error fetching or processing API data: {e}")

if __name__ == "__main__":
   employee_id = int(input("Enter employee ID: "))
   get_employee_todo_progress(employee_id)

