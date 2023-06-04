tasks = []

print("Welcome to Todo List Manager!")

while True:
    print("\nMenu:")
    print("1. Add Task")
    print("2. Mark Task as Completed")
    print("3. View Tasks")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        task_name = input("Enter task name: ")
        tasks.append(task_name)
        print("Task added successfully.")
    elif choice == "2":
        task_index = int(input("Enter the index of the task to mark as completed: "))
        if task_index >= 0 and task_index < len(tasks):
            tasks[task_index] = f"[Completed] {tasks[task_index]}"
            print("Task marked as completed.")
        else:
            print("Invalid task index.")
    elif choice == "3":
        if tasks:
            print("Tasks:")
            for index, task in enumerate(tasks):
                print(f"{index}. {task}")
        else:
            print("No tasks found.")
    elif choice == "4":
        task_index = int(input("Enter the index of the task to delete: "))
        if task_index >= 0 and task_index < len(tasks):
            deleted_task = tasks.pop(task_index)
            print(f"Task '{deleted_task}' deleted successfully.")
        else:
            print("Invalid task index.")
    elif choice == "5":
        print("Thank you for using Todo List Manager. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
