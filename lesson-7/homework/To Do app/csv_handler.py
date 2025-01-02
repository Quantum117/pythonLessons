import csv
from TaskManager import Task

class CSVHandler:
    def __init__(self, file_name):
        self.file_name = file_name

    def save(self, tasks):
        with open(self.file_name, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=["task_id", "name", "description", "status", "due_date"])
            writer.writeheader()
            for task in tasks:
                writer.writerow(task.to_dict())

    def load(self):
        try:
            with open(self.file_name, 'r') as f:
                reader = csv.DictReader(f)
                return [Task.from_dict(row) for row in reader]
        except FileNotFoundError:
            return []
