tasks = []

def show_tasks():
    if not tasks:
        print("\nNo tasks yet!")
    else:
        print("\nTasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task():
    task = input("\nEnter a new task: ")
    tasks.append(task)
    print(f"Task '{task}' added!")

def update_task():
    show_tasks()
    try:
        num = int(input("\nEnter task number to update: ")) - 1
        if 0 <= num < len(tasks):
            new_task = input("Enter the updated task: ")
            tasks[num] = new_task
            print("Task updated!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task():
    show_tasks()
    try:
        num = int(input("\nEnter task number to delete: ")) - 1
        if 0 <= num < len(tasks):
            print(f"Task '{tasks.pop(num)}' deleted!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    while True:
        print("\nMenu:")
        print("1. Show Tasks")
        print("2. Add Task")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Choose an option (1-5): ")

        if choice == "1":
            show_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            update_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()