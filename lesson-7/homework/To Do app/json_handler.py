import json
import os
from abstract_class import StorageInterface  # Assuming AbstractHandler is implemented in another module
from TaskManager import Task
class JSONHandler(StorageInterface):
    def __init__(self, filename):
        self.filename = filename

    def load(self):
        import json
        try:
            with open(self.filename, 'r') as file:
                data = json.load(file)  # Load tasks as a list of dictionaries
                return [Task.from_dict(task_dict) for task_dict in data]  # Convert each dict to Task
        except FileNotFoundError:
            print(f"File not found: {self.filename}. Starting with an empty task list.")
            return []  # Return an empty list if the file doesn't exist

        except json.JSONDecodeError as e:
            print(f"Error reading JSON file: {e}. Starting with an empty task list.")
            return []  # Return an empty list if JSON is malformed
        except Exception as e:
            print(f"Unexpected error while loading tasks: {e}")
            return []

    def save(self, tasks):
        try:
            with open(self.filename, 'w') as file:
                json.dump(tasks, file, indent=4)
            print(f"Tasks successfully saved to {self.filename}.")
        except Exception as e:
            print(f"Error saving tasks to file: {e}")
