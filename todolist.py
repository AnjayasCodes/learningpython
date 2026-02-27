is_running = True
choose = True
tasks = []
while is_running:
    print("Press 1 to add a Task")
    print("Press 2 to view the task")
    print("Press q to quit")

    choice = input("Choose a num: ")

    if choice == "1":
        choose = True
        while choose:
            decision = input("Do you want to add task(y or n):")
            if decision.lower() == "y":
                task = input("Write what you want to do: ")
                tasks.append(task)
            else:
                choose = False

    elif choice == "2":
        print("List of Things to Do")
        for task in tasks:
            print(task)
    elif choice == "q":
        print("Bye")
        is_running = False
    else:
        print("Invalid Choice")
