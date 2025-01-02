import os

# File name
FILE_NAME = "employees.txt"

# Ensure the file exists
def ensure_file_exists():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'w'):
            pass


# Add a new employee record
def add_employee():
    employee_id = input("Enter Employee ID: ").strip()
    name = input("Enter Name: ").strip()
    position = input("Enter Position: ").strip()
    salary = input("Enter Salary: ").strip()
    with open(FILE_NAME, 'a') as file:
        file.write(f"{employee_id}, {name}, {position}, {salary}\n")
    print("Employee record added successfully!\n")

# View all employee records
def view_employees():
    with open(FILE_NAME, 'r') as file:
        records = file.readlines()
    if records:
        print("Employee Records:")
        for record in records:
            print(record.strip())
    else:
        print("No employee records found.")
    print()

# Search for an employee by ID
def search_employee():
    search_id = input("Enter Employee ID to search: ").strip()
    with open(FILE_NAME, 'r') as file:
        for line in file:
            if line.startswith(search_id + ","):
                print("Employee Found:", line.strip())
                break
        else:
            print("Employee not found.")
    print()

# Update an employee record
def update_employee():
    search_id = input("Enter Employee ID to update: ").strip()
    updated = False
    with open(FILE_NAME, 'r') as file:
        records = file.readlines()
    with open(FILE_NAME, 'w') as file:
        for line in records:
            if line.startswith(search_id + ","):
                print("Current Record:", line.strip())
                name = input("Enter new Name (leave blank to keep current): ").strip()
                position = input("Enter new Position (leave blank to keep current): ").strip()
                salary = input("Enter new Salary (leave blank to keep current): ").strip()
                fields = line.strip().split(", ")
                if name: fields[1] = name
                if position: fields[2] = position
                if salary: fields[3] = salary
                file.write(", ".join(fields) + "\n")
                updated = True
                print("Employee record updated!\n")
            else:
                file.write(line)
    if not updated:
        print("Employee not found.\n")

# Delete an employee record
def delete_employee():
    search_id = input("Enter Employee ID to delete: ").strip()
    deleted = False
    with open(FILE_NAME, 'r') as file:
        records = file.readlines()
    with open(FILE_NAME, 'w') as file:
        for line in records:
            if line.startswith(search_id + ","):
                deleted = True
                print("Employee record deleted!\n")
            else:
                file.write(line)
    if not deleted:
        print("Employee not found.\n")

# Main menu
def main():
    ensure_file_exists()
    while True:
        print("Employee Records Manager")
        print("1. Add new employee record")
        print("2. View all employee records")
        print("3. Search for an employee by Employee ID")
        print("4. Update an employee's information")
        print("5. Delete an employee record")
        print("6. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            add_employee()
        elif choice == '2':
            view_employees()
        elif choice == '3':
            search_employee()
        elif choice == '4':
            update_employee()
        elif choice == '5':
            delete_employee()
        elif choice == '6':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
