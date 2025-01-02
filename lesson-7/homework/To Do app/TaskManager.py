from enum import Enum
from datetime import datetime

class Status(Enum):
    PENDING = "pending"
    IN_PROGRESS = "in progress"
    COMPLETED = "completed"

class Task:
    def __init__(self, task_id, title, description, status, due_date):
        self.task_id : int = int(task_id)
        self.title = title
        self.description = description
        self.status = status  # Use Status enum
        self.due_date = due_date  # Use datetime object

    def __str__(self):
        return f"Task ID: {self.task_id}, Title: {self.title}, Description:{self.description}, Status: {self.status.value}"

    def is_overdue(self):
        """Check if the task is overdue."""
        return datetime.now() > self.due_date


    def to_dict(self):
        """Convert Task to a dictionary."""
        return {
            "task_id": self.task_id,
            "title": self.title,
            "description": self.description,
            "status": self.status.value,
            "due_date": self.due_date.strftime('%Y-%m-%d'),
        }

    @staticmethod
    def from_dict(data):
        """Create a Task from a dictionary."""
        return Task(
            task_id=data["task_id"],
            title=data["title"],
            description=data["description"],
            status=Status(data["status"]),
            due_date=datetime.strptime(data["due_date"], '%Y-%m-%d')
        )


class TaskManager:
    def __init__(self):
        self.tasks = []  # List to store Task objects
        self.next_id = 1  # Incremental ID for new tasks

    def view_tasks(self):
        print("Tasks:")
        for task in self.tasks:
            print(f" {task.task_id}, {task.title}, {task.description}, {task.status.value}")

    def add_task(self, task: Task):
        """Add a new task."""
        self.tasks.append(task)
        self.next_id += 1

    def remove_task(self):
            task_id = self.get_task_id()
            if task_id :
                self.tasks = [task for task in self.tasks if task.task_id != int(task_id)]
                print(f"Task {task_id} removed successfully.")


    def update_task(self):
        """Update a task by its ID."""
        task_id = self.get_task_id()
        if  task_id:
         task = self.find_task(int(task_id))
         if task:
           updated_task = TaskManager.make_task_object()
           self.tasks[self.tasks.index(task)] = updated_task
        else:
           print("Task not found.")

    def filter_tasks (self):
          print("Completed Tasks:")
          print(*(task for task in self.tasks if task.status == Status.COMPLETED ), sep="\n")
          print("Pending Tasks : ")
          print(*(task for task in self.tasks if task.status == Status.PENDING), sep="\n")
          print("In Progress Tasks :")
          print(*(task for task in self.tasks if task.status == Status.IN_PROGRESS), sep="\n")

    def list_tasks(self):
        """List all tasks."""
        return [task.to_dict() for task in self.tasks]

    def find_task(self, task_id):
        """Find a task by ID."""
        for task in self.tasks:
            if task.task_id == task_id:
                return task
        return None

    def save_tasks(self, handler):
        """Save tasks using a specific file format handler."""
        handler.save(self.tasks)
        print("Tasks saved successfully.")

    def load_tasks(self, handler):
        """Load tasks using a specific file format handler."""
        self.tasks = handler.load()
        self.next_id = max((task.task_id for task in self.tasks), default=0) + 1
        print("Tasks loaded successfully.")

    @staticmethod
    def get_task_id():
        """gets task id by input validation with try/except block"""
        try:
            task_id = input("Enter Task ID : ").strip()
            if not task_id.isdigit():
                raise ValueError("Task ID must be numeric.")
            return int(task_id)
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")
            return None

    @staticmethod
    def make_task_object():
        try:
            task_id = input("Enter Task ID : ").strip()
            if not task_id.isdigit():
                raise ValueError("Task ID must be numeric.")

            title = input("Enter Title: ").strip()
            if not title:
                raise ValueError("Title cannot be empty.")

            description = input("Enter Description: ").strip()
            if not description:
                raise ValueError("Description cannot be empty.")


            due_date = input("Enter due date (YYYY-MM-DD): ")
            if  due_date:
                try:
                    # Attempt to convert the input string to a datetime object
                    due_date = datetime.strptime(due_date, "%Y-%m-%d")
                    print(f"Due date updated to {due_date.strftime('%Y-%m-%d')}")
                except ValueError:
                    # If the conversion fails, print an error message
                    print("Invalid date format. Please enter the date in YYYY-MM-DD format.")

            status = input("Enter task status (Pending, In Progress, Completed): ").strip().lower()
            if status not in [s.value for s in Status]:
                raise ValueError("Invalid status.")

            status = Status(status)
            print("Task added successfully!")
            return Task(task_id, title, description, status, due_date)

        except ValueError as e:
           print(f"Invalid input: {e}. Please try again.")
