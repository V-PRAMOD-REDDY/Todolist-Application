# To-do list application
Tasks_list = []

# Add a task to the Tasks_list
def add_task():
    task = input("Enter the task: ")
    Tasks_list.append({"task": task, "completed": False})
    print(f"Task '{task}' added successfully.")

# delete a task from Tasks_list
def delete_task():
    task = input("Enter the task to delete: ")
    for item in Tasks_list:
        if item["task"] == task:
            Tasks_list.remove(item)
            print(f"Task '{task}' deleted successfully.")
            return
    print(f"Task '{task}' not found.")

#display the list of tasks
def display_tasks():
    if not Tasks_list:
        print("No tasks in the to-do list.")
    else:
        print("To-Do List:")
        for index, item in enumerate(Tasks_list, start=1):
            status = "Completed" if item["completed"] else "Not Completed"
            print(f"{index}. {item['task']} - {status}")

# mark a task as complete
def mark_complete():
    task = input("Enter the task to mark as complete: ")
    for item in Tasks_list:
        if item["task"] == task:
            item["completed"] = True
            print(f"Task '{task}' marked as complete.")
            return
    print(f"Task '{task}' not found.")

if __name__ == "__main__":
    print("Welcome! to the To_do list Application:)")
    while True:
        print("\n")
        print("Please select one of the following options:")
        print("-------------------------------------------")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. Display Tasks")
        print("4. Mark Task as Complete")
        print("5. Quit")

        choice = input("Enter your choice (1-5):")

        if choice == "1":
            add_task()
        elif choice == "2":
            
            delete_task()
        elif choice == "3":
            display_tasks()
        elif choice == "4":
            
            mark_complete()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

    