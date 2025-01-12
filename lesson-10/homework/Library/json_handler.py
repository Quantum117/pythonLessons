import json
import os

class JSONHandler:
    def __init__(self, filename):
        self.filename = filename

    def load(self):
        try:
            with open(self.filename, 'r') as file:
                objects = json.load(file)
                if not isinstance(objects, list):  # Ensure objects are in a valid format
                    raise ValueError("JSON file format is invalid: expected a list of objects.")
                return objects
        except FileNotFoundError:
            print(f"File '{self.filename}' not found. Starting with an empty task list.")
            return []  # Return an empty list if file doesn't exist
        except json.JSONDecodeError as e:
            print(f"Error reading JSON file: {e}. Starting with an empty task list.")
            return []  # Return an empty list if JSON is malformed
        except Exception as e:
            print(f"Unexpected error while loading objects: {e}")
            return []

    def save(self, tasks):
        try:
            with open(self.filename, 'w') as file:
                json.dump(tasks, file, indent=4)
            print(f"Tasks successfully saved to {self.filename}.")
        except Exception as e:
            print(f"Error saving tasks to file: {e}")
