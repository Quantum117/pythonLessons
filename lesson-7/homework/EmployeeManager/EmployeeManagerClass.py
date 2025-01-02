import os

"""
This module defines two main classes, `Employee` and `EmployeeManager`, that work together to manage 
an Employee Records System. 

Classes:
--------
1. **Employee**:
    - Represents individual employee data with fields for ID, name, position, and salary.
    - Includes:
        - `employee_id`: (int) Unique identifier for the employee.
        - `name`: (str) Employee's full name.
        - `position`: (str) Job position/title of the employee.
        - `salary`: (float) Employee's salary.
    - Methods:
        - `__init__(self, employee_id, name, position, salary)`:
        Initializes an employee instance with the specified attributes.
        - `__str__(self)`: Provides a string representation of the employee instance.

2. **EmployeeManager**:
    - Handles operations related to managing a collection of employees through a file-based storage system (`filename`).
    - Promotes a persistent and easy-to-use way of adding, viewing, sorting, searching, updating, and deleting employee records.

    - Attributes:
        - `filename`: (str) Path to the file where employee data is stored.
    - Methods:
        - `__init__(self, filename)`: Sets up the repository for employee records.
        - `add_employee(self, employee)`: Adds a new employee record to the file.
        - `view_employees(self)`: Displays all employee records from the file.
        - `sort_employees(self)`: Provides multiple sorting options (e.g., by salary or name).
        - `search_employee(self)`: Searches for an employee by Employee ID.
        - `update_employee(self)`: Updates an existing employee's information by Employee ID.
        - `delete_employee(self)`: Removes an employee record by Employee ID.
        - `unique_id(self, _id)`: Ensures that the given employee ID is unique across all employee records.
        - `make_employee_object(self)`: Interacts with the user to create an `Employee` object through prompts and validation.
        - `save_employee_to_file(employee, filename)`: (Static) Saves an `Employee` instance to the specified file.
        - `str_to_employee(line)`: (Static) Converts a string representation of an employee to an `Employee` object.
        - `file_to_list(self)`: Reads the file and converts its content into a list of `Employee` objects.
"""

# Employee class , encapsulates individual employee data in it
class Employee:
    def __init__(self, employee_id , name, position, salary):
        self.employee_id = int(employee_id)
        self.name = name
        self.position = position
        self.salary = float(salary)

    def __str__(self):
        return f"ID: {self.employee_id}, Name: {self.name}, Position: {self.position}, Salary: {self.salary}"


class EmployeeManager:
    def __init__(self, filename):
        self.filename = filename
        if not os.path.exists(self.filename):
            with open(self.filename, 'w'):
                pass


    def add_employee(self, employee:Employee):
        employee_id : int = employee.employee_id
        name = employee.name
        position = employee.position
        salary = employee.salary
        with open(self.filename, 'a') as file:
            file.write(f"{employee_id}, {name}, {position}, {salary}\n")
        print("Employee added successfully!\n")

    def view_employees(self):
        with open(self.filename, 'r') as file:
            records = file.readlines()
        if records:
            print("Employee Records:")
            for record in records:
                print(record.strip())
        else:
            print("No employee records found.")
        print()

    def sort_employees(self):
        print("Choose a sorting option:")
        print("1. Sort by Salary (Ascending)")
        print("2. Sort by Salary (Descending)")
        print("3. Sort by Name (Ascending)")
        print("4. Sort by Name (Descending)")
        print("5. Sort by Salary, then Name (Ascending)")

        choice = input("Enter your choice (1-5): ").strip()
        employees = self.file_to_list()
        if choice == "1":
            sorted_employees = sorted(employees, key=lambda emp: emp.salary)
        elif choice == "2":
            sorted_employees = sorted(employees, key=lambda emp: emp.salary, reverse=True)
        elif choice == "3":
            sorted_employees = sorted(employees, key=lambda emp: emp.title)
        elif choice == "4":
            sorted_employees = sorted(employees, key=lambda emp: emp.title, reverse=True)
        elif choice == "5":
            sorted_employees = sorted(employees, key=lambda emp: (emp.salary, emp.title))
        else:
            print("Invalid choice. No sorting performed.")
            return

        print("\nSorted Employees:")
        for item in sorted_employees:
            print(item)

    # Search for an employee by ID
    def search_employee(self):
        search_id = input("Enter Employee ID to search: ").strip()
        with open(self.filename, 'r') as file:
            for line in file:
                if line.startswith(search_id + ","):
                    print("Employee Found:", line.strip())
                    break
            else:
                print("Employee not found.")
        print()


    def update_employee(self):
        search_id = input("Enter Employee ID to update: ").strip()
        updated = False
        with open(self.filename, 'r') as file:
            records = file.readlines()
        with open(self.filename, 'w') as file:
            for line in records:
                if line.startswith(search_id + ","):
                    print("Current Record:", line.strip())
                    employee = self.make_employee_object()
                    file.write(f"{employee.employee_id},{employee.name},{employee.position},{employee.salary}\n")
                    updated = True
                    print("Employee record updated!\n")
                else:
                    file.write(line)
        if not updated:
            print("Employee not found.\n")

    # Delete an employee record
    def delete_employee(self):
        search_id = input("Enter Employee ID to delete: ").strip()
        deleted = False
        with open(self.filename, 'r') as file:
            records = file.readlines()
        with open(self.filename, 'w') as file:
            for line in records:
                if line.startswith(search_id + ","):
                    deleted = True
                    print("Employee record deleted!\n")
                else:
                    file.write(line)
        if not deleted:
            print("Employee not found.\n")

    def unique_id(self, _id: int):
        employees = self.file_to_list()
        employee_ids = (emp.employee_id for emp in employees)
        if _id in employee_ids:
            return False
        else:
            return True


    def make_employee_object(self):

        try:
            employee_id = input("Enter Employee ID (numeric): ").strip()
            if not employee_id.isdigit():
                raise ValueError("Employee ID must be numeric.")

            if not self.unique_id( int(employee_id)):
                raise ValueError("Employee ID already exists.")

            name = input("Enter Name: ").strip()
            if not name:
                raise ValueError("Name cannot be empty.")

            position = input("Enter Position: ").strip()
            if not position:
                raise ValueError("Position cannot be empty.")

            salary = input("Enter Salary (numeric): ").strip()
            if not salary.isdigit():
                raise ValueError("Salary must be numeric.")

            return Employee(employee_id, name, position, float(salary))

        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")


    @staticmethod
    def save_employee_to_file( employee: Employee, filename):
        try:
            with open(filename, "a") as file:
                file.write(f"{employee.employee_id},{employee.name},{employee.position},{employee.salary}\n")
            print("Employee saved successfully.")
        except IOError as e:
            print(f"File operation failed: {e}")

    @staticmethod
    def str_to_employee (line: str):
        employee_id, name, position, salary = line.split(",")
        return Employee(employee_id.strip(), name.strip(), position.strip(), salary.strip())

    def file_to_list (self):
        records = []
        with open(self.filename, "r") as file:
            for line in file:
                records.append(self.str_to_employee(line))
        return records