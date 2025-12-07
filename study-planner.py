from datetime import datetime, timedelta
import operator

task_list = []

def add_task():
    name = input("Enter task name: ")
    deadline_str = input("Enter due date (YYYY-MM-DD): ")
    deadline = datetime.strptime(deadline_str, "%Y-%m-%d")
    priority_level = input("Enter priority level (High/Medium/Low): ").capitalize()

    task_list.append({
        "name": name,
        "deadline": deadline,
        "priority level":priority_level,
        "status" : "Pending"
    })
    print(f"Task '{name}' successfully added!")

def view_task():
    if task_list == False:
        print("There is no task.")
        return
    
    print("\nAll Task: ")
    print("-" * 50)
    for i, task in enumerate(task_list, start = 1):
        print(f"For Task {i}:")
        print(f"Name        :{task['name']}")
        print(f"Deadline    :{task['deadline']}")
        print(f"Priority    :{task['priority level']}")
        print(f"Status      :{task['status']}")
        print("-" * 50)


def sort_tasks():
    if not task_list:
        print("No tasks to sort.")
        return

    priority_order = {'High': 1, 'Medium': 2, 'Low': 3}

    sorted_tasks = sorted(
        task_list,
        key=lambda task: (
            (datetime.strptime(task['deadline'], "%Y-%m-%d") - datetime.now()).days,
            priority_order.get(task['priority level'], 99)
        )
    )

    print("\n=== Tasks Sorted by Days Left & Priority ===")
    print("-" * 50)

    for task in sorted_tasks:
        days_left = (datetime.strptime(task['deadline'], "%Y-%m-%d") - datetime.now()).days

        print(f"Task Name   : {task['name']}")
        print(f"Days Left   : {days_left}")
        print(f"Priority    : {task['priority level']}")
        print("-" * 50)

def edit_task():
    if task_list == []:
        print("No task to edit")
        return

    print("\n===Current Task===")
    for i, task in enumerate(task_list, start = 1):
        print(f"{i}. {task['name']} (Status: {task['status']})")

    choice = int(input("Enter the task's number you want to edit: "))

    if choice < 1 or choice > (len(task_list)):
        print("Invalid Choice")
        return
    
    task = task_list[choice - 1]

    print("\nWhat do you want to edit?")
    print("1. Name")
    print("2. Deadline")
    print("3. Priority Level")
    print("4. Status")

    edit_choice = int(input("Enter your choice (1-4): "))

    if edit_choice == 1:
        new_name = input("Enter new task name: ")
        task['name'] = new_name
        print("Task name updated successfully!")
    elif edit_choice == 2:
        new_deadline_str = input("Enter new due date (YYYY-MM-DD): ")
        new_deadline = datetime.strptime(new_deadline_str, "%Y-%m-%d")
        task['deadline'] = new_deadline
        print("Task deadline updated successfully!")
    elif edit_choice == 3:
        new_priority = input("Enter new priority level (High/Medium/Low): ").capitalize()
        task['priority level'] = new_priority
        print("Task priority level updated successfully!")
    elif edit_choice == 4:
        new_status = input("Enter new status (Pending/Completed): ").capitalize()
        task['status'] = new_status
        print("Task status updated successfully!")
    else:
        print("Invalid choice")
        return
    
    print("Task updated successfully!")

def delete_task():
    if task_list == []:
        print("No task to delete")
        return

    print("\n===Current Task===")
    for i, task in enumerate(task_list, start = 1):
        print(f"{i}. {task['name']} (Status: {task['status']})")

    choice = int(input("Enter the task's number you want to delete: "))

    if choice < 1 or choice > (len(task_list)):
        print("Invalid Choice")
        return
    
    deleted_task = task_list.pop(choice - 1)
    print(f"Task '{deleted_task['name']}' deleted successfully!")

def mark_task_completed():
    if task_list == []:
        print("No task to mark as completed")
        return

    print("\n===Current Task===")
    for i, task in enumerate(task_list, start = 1):
        print(f"{i}. {task['name']} (Status: {task['status']})")

    choice = int(input("Enter the task's number you want to mark as completed: "))

    if choice < 1 or choice > (len(task_list)):
        print("Invalid Choice")
        return
    
    task = task_list[choice - 1]
    task['status'] = "Completed"
    print(f"Task '{task['name']}' marked as completed!")

def main():
    while True:
        print("\nStudy Planner Menu:")
        print("1. Add Task")
        print("2. View Sorted Tasks")
        print("3. View Tasks")
        print("4. Edit Task")
        print("5. Delete Task")
        print("6. Mark Task as Completed")
        print("7. Exit")

        choice = int(input("Enter your choice (1-6): "))

        if choice == 1:
            add_task()
        elif choice == 2:
            sort_tasks()
        elif choice == 3:
            view_task()
        elif choice == 4:
            edit_task()
        elif choice == 5:
            delete_task()
        elif choice == 6:
            mark_task_completed()
        elif choice == 7:
            print("Exiting Study Planner. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
        

if __name__ == "__main__":
    main()
