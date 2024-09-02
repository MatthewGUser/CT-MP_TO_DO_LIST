# Included to stall menu to look at output of previous input
import time

# Output the Menu
def display_menu():
    print("\nWelcome to the To-Do List App!")
    print("Menu:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Mark a task as complete")
    print("4. Delete a task")
    print("5. Quit")

# Add new task
def add_task(tasks):
    try:
        title = input("Enter the task title: ").strip()
        if not title:
            raise ValueError("Task title cannot be empty.")
        tasks.append({"title": title, "status": "Incomplete"})
        print(f"\nTask '{title}' added successfully.")
    except ValueError as e:
        print(f"Error: {e}")

# View all tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks to display.")
        return
    print("\nCurrent tasks:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task['title']} - {task['status']}")

# Mark task as finished
def mark_task_complete(tasks):
    try:
        view_tasks(tasks)
        task_number = int(input("Enter the task number to mark as complete: "))
        if task_number < 1 or task_number > len(tasks):
            raise IndexError("Task number out of range.")
        tasks[task_number - 1]["status"] = "Complete"
        print(f"Task '{tasks[task_number - 1]['title']}' marked as complete.")
    except (ValueError, IndexError) as e:
        print(f"Error: {e}")

# Delete a specific task
def delete_task(tasks):
    try:
        view_tasks(tasks)
        task_number = int(input("Enter the task number to delete: "))
        if task_number < 1 or task_number > len(tasks):
            raise IndexError("Task number out of range.")
        removed_task = tasks.pop(task_number - 1)
        print(f"Task '{removed_task['title']}' deleted.")
    except (ValueError, IndexError) as e:
        print(f"Error: {e}")

# Code hub
def main():

    tasks = []
    
    while True:
        display_menu()

        # Pick from menu options:
        choice = input("Select an option (1-5): ").strip()
        try:
            if choice == "1":
                add_task(tasks)
            elif choice == "2":
                view_tasks(tasks)
            elif choice == "3":
                mark_task_complete(tasks)
            elif choice == "4":
                delete_task(tasks)
            elif choice == "5":
                print("Exiting the application. Thank you!")
                break
            else:
                raise ValueError("Invalid choice. Please select a number between 1 and 5.")
        except ValueError as e:
            print(f"Error: {e}")
            
        #! Set to 0 if you want to remove stall
        time.sleep(1) # Stall for 1 second to see output

# Execute program
if __name__ == "__main__":
    main()
