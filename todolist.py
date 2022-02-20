mytasks = []
current = int(input("What would you like to do? \n1. Add a task \n2. Remove a task \n3. View tasks \n4. Exit \nInput: "))

while current != 4:
    if current == 1:
        taskname = input("Enter your task name: ")
        duedate = input("Enter due date (Day or date, time): ")
        mytasks.append(f"{taskname} (Due date: {duedate})")
    elif current == 2:
        print(mytasks)
        numberdel = int(input("Which task number would you like to delete? "))
        mytasks.pop(numberdel - 1)
    elif current == 3:
        print(f"Your tasks: {mytasks}")
    else:
        break
    current = int(input("What would you like to do? \n1. Add a task \n2. Remove a task \n3. View tasks \n4. Exit \nInput: "))

print("Looking forward to keeping more of your tasks!")
