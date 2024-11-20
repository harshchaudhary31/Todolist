import os

def add_task(tasks):
    task = input("Enter a new task: ")
    tasks.append({"task": task, "completed": False})
    print("Task added!")

def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return
    for i, task in enumerate(tasks, 1):
        status = "Done" if task["completed"] else "Pending"
        print(f"{i}. {task['task']} [{status}]")

def mark_completed(tasks):
    view_tasks(tasks)
    task_num = int(input("Enter task number to mark as completed: "))
    if 1 <= task_num <= len(tasks):
        tasks[task_num - 1]["completed"] = True
        print("Task marked as completed!")
    else:
        print("Invalid task number.")

def save_tasks(tasks, filename="tasks.txt"):
    with open(filename, "w") as file:
        for task in tasks:
            file.write(f"{task['task']},{task['completed']}\n")
    print("Tasks saved!")

def load_tasks(filename="tasks.txt"):
    if not os.path.exists(filename):
        return []
    with open(filename, "r") as file:
        return [
            {"task": line.split(",")[0], "completed": line.split(",")[1].strip() == "True"}
            for line in file.readlines()
        ]

def main():
    tasks = load_tasks()
    while True:
        print("\nTo-Do List")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task Completed")
        print("4. Save and Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_completed(tasks)
        elif choice == "4":
            save_tasks(tasks)
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
