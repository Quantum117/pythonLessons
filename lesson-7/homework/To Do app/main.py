from TaskManager import  TaskManager
from json_handler import JSONHandler
from csv_handler import CSVHandler
'''
    I wrote different handlers for json(json_handler) and csv(csv_handler) files in different modules .
    TaskManager class has two methods that accepts handler object as an argument 
    and calls appropriate method of handler object.Each handler class must have load() and save() methods. 
    This is ensured by creating abstract class (with save() and load() abstract methods ) 
    that each file handler class must inherit from.
    So in this way our program is flexible and independent of file format. If we want to add a support for  
    new file format we only need to add new handler class with load and save methods and change main function a little .
'''
def main():

    # in this part  we are specifying file format to work with  user input before to do app menu appears.
    task_manager = TaskManager()
    json_handler = JSONHandler("tasks.json")
    csv_handler = CSVHandler("tasks.csv")

    handler = input("enter file handler format (json/csv): ")

    if handler == "json" or handler.strip() == "":
        handler = json_handler
    if handler == "csv":
        handler = csv_handler
    # load tasks after specifying handler format
    task_manager.load_tasks(handler)
    print()

    # To do app menu
    print("Welcome to the To-Do Application!")
    print("1. Add a new Task")
    print("2. View all Tasks")
    print("3. Update a Task")
    print("4. Delete a Task")
    print("5. Filter tasks by status")
    print("6. Save tasks")
    print("7. Load tasks")
    print("8. Exit")

    # while loop that runs until exit
    while True:
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            task = TaskManager.make_task_object()

            if task:  # Ensure task is not None before proceeding
                task_manager.add_task(task)

            # there is no need in else block,we have input validation in make_task_object() method
            # so it already notifies user if some exception thrown before returning None

        elif choice == '2':
            task_manager.view_tasks()

        elif choice == '3':
            task_manager.update_task()

        elif choice == '4':
            task_manager.remove_task()

        elif choice == '5':
            task_manager.filter_tasks()

        elif choice == '6':
            task_manager.save_tasks(handler)

        elif choice == '7':
            task_manager.load_tasks(handler)

        elif choice == '8':
            print("Goodbye!")
            # save tasks before exiting
            task_manager.save_tasks(handler)
            break
        else:
            print("Invalid choice. Please try again.\n")


if __name__ == "__main__":
    main()