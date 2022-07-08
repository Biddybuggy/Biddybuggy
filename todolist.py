import json

mylist = []
current = int(input("What would you like to do? \n1. Add a task \n2. Remove or complete a task \n3. View your to-do list \n4. Save your tasks \n5. Quit \nInput: "))
while current != 5:
    if current == 1:
        task = input("\nEnter task name: ")
        duedate = input("Enter due date: ")
        mylist.append(f"{task} (Due date: {duedate})")
        
    elif current == 2:
        if mylist == []:
            print("\nYour To-Do List is empty!")
        else:
            print("\nYour Tasks")
            for each_item in mylist:
                print(each_item)
            removedtask = int(input("Which task would you like to remove or complete (enter task's number from the top): "))
            mylist.pop(removedtask - 1)

    elif current == 3:
        if mylist == []:
            print("\nWoohoo! You don't have any tasks to do!")
        else:
            print("\nYour Tasks")
            for each_item in mylist:
                print(each_item)

    elif current == 4:
        print("\nSaving your tasks!")
        jsonList = json.dumps(mylist)
        jsonFile = open("path","w")
        jsonFile.write(jsonList)
        jsonFile.close()
        print("\nYour tasks have been saved!")
        
    elif current < 1 or current > 5:
        print("\nInvalid Input!")

    current = int(input("\nWhat would you like to do? \n1. Add a task \n2. Remove or complete a task \n3. View your to-do list \n4. Save your tasks \n5. Quit \nInput: "))

print("\nThanks for using To-Do List!")
