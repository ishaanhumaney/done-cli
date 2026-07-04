import json
import os

TODO_FILE = "todo_list.json"


def load_tasks():
    if not os.path.exists(TODO_FILE):
        return []
    try:
        with open(TODO_FILE, "r") as f:  # Modified to fit file context
            return json.load(f)
    except json.JSONDecodeError:
        print("Warning: Corrupted save file. Starting with an empty list.")
        return []


def save_tasks(tasks):
    with open(TODO_FILE, "w") as f:
        json.dump(tasks, f, indent=4)


def show_tasks(tasks):
    if not tasks:
        print("\nYour to-do list is empty.")
        return

    print("\n--- Current Tasks ---")
    for i, task in enumerate(tasks, 1):
        status = "✓" if task["completed"] else " "
        print(f"{i}. [{status}] {task['title']}")


def add_task(tasks):
    title = input("\nEnter task description: ").strip()
    if title:
        tasks.append({"title": title, "completed": False})
        save_tasks(tasks)
        print(f"Added: '{title}'")
    else:
        print("Task description cannot be empty.")


def toggle_task(tasks):
    show_tasks(tasks)
    if not tasks:
        return

    try:
        choice = int(input("\nEnter the number of the task to toggle: "))
        if 1 <= choice <= len(tasks):
            tasks[choice - 1]["completed"] = not tasks[choice - 1]["completed"]
            save_tasks(tasks)
            print("Task status updated.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


def delete_task(tasks):
    show_tasks(tasks)
    if not tasks:
        return

    try:
        choice = int(input("\nEnter the number of the task to delete: "))
        if 1 <= choice <= len(tasks):
            removed = tasks.pop(choice - 1)
            save_tasks(tasks)
            print(f"Deleted: '{removed['title']}'")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


def main():
    tasks = load_tasks()

    while True:
        print("\n=== To-Do List ===")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Toggle Complete")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            toggle_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()