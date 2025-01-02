import json
from TaskManager import Task
from abstract_class import StorageInterface

class JSONHandler(StorageInterface):
    def __init__(self, file_name):
        self.file_name = file_name

    def save(self, tasks):
        with open(self.file_name, 'w') as f:
            json.dump([task.to_dict() for task in tasks], f, indent=4)

    def load(self):
        try:
            with open(self.file_name, 'r') as f:
                data = json.load(f)
                # returns list of task objects from json
                return [Task.from_dict(task) for task in data]
        except FileNotFoundError:
            return []
