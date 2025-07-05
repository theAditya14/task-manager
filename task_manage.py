import json
import os

filename = "data.saver"

def add_task():
    task_name = input("Enter task name: ")
    deadline = input("Enter deadline(dd-mm-yyy): ")
    priority = input("Enter the task priority(Easy,Medium,Hard): ")
    status = input("task status(pending/done): ")

    task_data = {
        "task_name" : task_name,
        "deadline" : deadline,
        "priority" : priority,
        "status" : status
    }

    tasks = []

    if os.path.exists(filename):
         with open(filename,'r') as file:
             try:
                tasks = json.load(file)
             except json.JSONDecodeError:
                 tasks = []

    tasks.append(task_data)

    with open(filename,'w') as file:
        json.dump(tasks,file,indent=4)
        

def view_all_task():
        if not os.path.exists(filename):
               print("Sorry file is not found!")
               return
        with open(filename, "r") as file:
          try:
            tasks = json.load(file)
            for i, task in enumerate(tasks, start=1):
                print(f"\nTask {i}:")
                for key, value in task.items():
                    print(f"{key.capitalize()}: {value}")
                print("--------------")
          except json.JSONDecodeError:
            print("File is empty or corrupted.")

def mark_task_complete():
   
    if not os.path.exists(filename):
        print("No tasks found.")
        return

    # Step 1: Load tasks
    with open(filename, "r") as file:
        try:
            tasks = json.load(file)
        except json.JSONDecodeError:
            print("File is empty or broken.")
            return

    # Step 2: Show tasks with numbers
    print("\nYour Tasks:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task['task_name']} - Status: {task['status']}")

    # Step 3: Ask user to select task number
    try:
        choice = int(input("\nEnter the task number to mark as done: "))
        if 1 <= choice <= len(tasks):
            tasks[choice - 1]['status'] = 'done'
            print("Task marked as done.")
        # elif tasks[choice - 1]['status']  == 'done' and 1 <= choice <= len(tasks):
        #         print("This task is already completed")
        else:
            print("⚠️ Invalid task number.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    # Step 4: Save updated list
    with open(filename, "w") as file:
        json.dump(tasks, file, indent=4)

def delete_task():
    if not os.path.exists(filename):
        print("No tasks found.")
        return

    with open(filename, "r") as file:
        try:
            tasks = json.load(file)
        except json.JSONDecodeError:
            print("File is empty or broken.")
            return
        
    if not tasks:
        print("📭 No tasks to delete.")
        return
        
        
    print("\nYour Tasks:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task['task_name']} - Status: {task['status']}")

    try:
       choice = int(input("which task you want to delete: "))
       if 1 <= choice <= len(tasks):
         delete = tasks.pop(choice-1)
         print(f"✅ Deleted task: {delete['task_name']}")
       else:
            print("⚠️ Invalid task number.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return
    
    with open(filename, "w") as file:
        json.dump(tasks, file, indent=4)

while True:

    print("Add_task(1)")
    print("view_all_task(2)")
    print("mark_task_completed(2)")
    print("delete_task(4)")
    print("Exit__(5)")
    print("-------------")

    choice = int(input("Enter here: "))
    if choice == 1:
         add_task()
    elif choice ==2:    
        view_all_task()
    elif choice ==3:
         mark_task_complete()
    elif choice ==4:
          delete_task()
    elif choice == 5:
        print("system close.....")
        break
    else:
        print("Sorry invalid syntax(1,2,3,4,5..)")


