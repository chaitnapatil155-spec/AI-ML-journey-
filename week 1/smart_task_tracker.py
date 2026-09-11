def add_task():
    task = input("enter your task:-")
    with open ("task_dataset.txt","a") as file:
        file.write(task + "\n")
        file.flush()
    print("task saved successfully!")

def view_tasks():
    try:
      with open ("task_dataset.txt","r") as file:
          task = file.read()
          if task.strip() == "":
              print("your task is empty!")
          else:
              print("--- your task list---")    
              print(task)
    except FileNotFoundError:
        print("no tasks found!")

def main_menu()  :
    while True:
        print("\n" + "="*40)
        print("  smart ai_task tracker  ") 
        print("="*30)
        print("1. ada a new task")
        print("2. view all tasks")
        print("3. exit")
        print("="*30)

        try:
            choice = int(input("enter your choice (1-3):")) 

            if choice == 1:
                add_task()
            elif choice == 2:
                view_tasks() 
            elif choice == 3:
                print("exiting the program. goodbye!") 
                break 

            else:
                print("invalid choice! please enter a number between 1-3 ")
        except ValueError:
            print("error: please enter digits only ( 1,2, or 3)!")                                
main_menu()
