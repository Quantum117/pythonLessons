from EmployeeManagerClass import EmployeeManager

# Main menu
def main():
    print("Employee Records Manager")
    print("1. Add new employee record")
    print("2. View all employee records")
    print("sort. Sort employee records before displaying")
    print("3. Search for an employee by Employee ID")
    print("4. Update an employee's information")
    print("5. Delete an employee record")
    print("6. Exit")

    while True:

        choice = input("Enter your choice: ").strip()
        emp_class = EmployeeManager('employees.txt')
        if choice == '1':
            new_employee = emp_class.make_employee_object()

            if new_employee:  # Ensure new_employee is not None before proceeding
                emp_class.add_employee(new_employee)
            # there is no need in else block,we have input validation in make_employee_object() method
            # so it already notifies user before returning None

        elif choice == '2':
            emp_class.view_employees()
        elif choice.strip() == 'sort':
            emp_class.sort_employees()
        elif choice == '3':
            emp_class.search_employee()
        elif choice == '4':
            emp_class.update_employee()
        elif choice == '5':
            emp_class.delete_employee()
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()

