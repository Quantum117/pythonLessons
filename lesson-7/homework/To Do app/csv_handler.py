import csv
from TaskManager import Task
from abstract_class import StorageInterface

class CSVHandler(StorageInterface):
    def __init__(self, file_name):
        self.file_name = file_name

    def save(self, tasks):
        try:
            with open(self.file_name, 'w', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=["task_id", "name", "description", "status", "due_date"])
                writer.writeheader()
                for task in tasks:
                    writer.writerow(task.to_dict())
            print(f"Tasks successfully saved to {self.file_name}.")
        except PermissionError:
            print(f"Permission denied: Unable to write to file '{self.file_name}'.")
        except Exception as e:
            print(f"Unexpected error while saving tasks to CSV: {e}")

    def load(self):
        try:
            with open(self.file_name, 'r') as f:
                reader = csv.DictReader(f)
                return [Task.from_dict(row) for row in reader]
        except FileNotFoundError:
            print(f"File '{self.file_name}' not found. Starting with an empty task list.")
            return []  # Return an empty list if file doesn't exist
        except csv.Error as e:
            print(f"Error reading CSV file: {e}. Starting with an empty task list.")
            return []  # Return an empty list if CSV is malformed
        except Exception as e:
            print(f"Unexpected error while loading tasks from CSV: {e}")
            return []
