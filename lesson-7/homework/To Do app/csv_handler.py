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
        import csv
        try:
            tasks = []
            with open(self.file_name, mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    # Convert each row (a dictionary) into a Task object
                    task_data = {
                        "task_id": int(row["task_id"]),
                        "title": row["title"],
                        "description": row["description"],
                        "status": row["status"],
                        "due_date": row["due_date"],
                    }
                    tasks.append(Task.from_dict(task_data))
            return tasks
        except FileNotFoundError:
            print(f"File not found: {self.filename}. Starting with an empty task list.")
            return []  # Return an empty list if the file doesn't exist
        except csv.Error as e:
            print(f"Error reading CSV file: {e}. Starting with an empty task list.")
            return []  # Return an empty list if CSV is malformed
        except Exception as e:
            print(f"Unexpected error while loading tasks from CSV: {e}")
            return []
