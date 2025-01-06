import json
from abstract_class import StorageInterface  # Assuming AbstractHandler is implemented in another module

class JSONHandler(StorageInterface):
    def __init__(self, filename):
        self.filename = filename

    def load(self):
        try:
            with open(self.filename, 'r') as file:
                tasks = json.load(file)
                if not isinstance(tasks, list):  # Ensure tasks are in a valid format
                    raise ValueError("JSON file format is invalid: expected a list of tasks.")
                return tasks
        except FileNotFoundError:
            print(f"File '{self.filename}' not found. Starting with an empty task list.")
            return []  # Return an empty list if file doesn't exist
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
