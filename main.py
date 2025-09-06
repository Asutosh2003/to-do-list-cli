tasks = []
def show_task():
    if len(tasks)==0:
        print(" \033[93m No tasks Yet.  \033[0m")
    else:
        for items in range(1,len(tasks)+1):
            print(f"{items}. {tasks[items-1]}")
# show_task()
def add_task(task):
    tasks.append(task)
    print("\033[97m --Task added successfully-- \033[0m")
def delete_task(id: int):
    if 0<id<=len(tasks):
        print(f"Task {tasks[id-1]} deleted successfully")
        tasks.pop(id-1)
        
    else:
        print("\033[91m Please enter a valid task id.\033[0m")
# show_task()
# delete_task(3)
# show_task()
while True:
    print("\033[94m\n ------ To Do List App  ------ \033[0m")
    print("\033[96m 1. View Task \033[0m")
    print("\033[96m 2. Add Task \033[0m")
    print("\033[96m 3. Delete Task \033[0m")
    print("\033[96m 4. Exit \033\033[0m")
    
    try:
        choice = int(input(" Please Choose an option from the above :- "))
    except Exception as e:
        print(e)
        continue
    
    if choice == 1:
        print("\033[92m Current Tasks :- \033[0m")
        show_task()
        print("----  End ----")
    elif choice == 2:
        new_task:str = input("Please enter a Task to add ")
        add_task(new_task)
    elif choice == 3:
        show_task()
        id = int(input("Enter the task number you want to delete"))
        delete_task(id)
    elif choice == 4:
        print("\033[95m-- You have been exited successfully -- \033[0m")
        break
    else:
        print(" \n ")
        print("\033[91m Please choose an valid option from the above\033[0m")


