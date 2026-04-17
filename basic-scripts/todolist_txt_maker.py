# To-Do List Maker
# I am going to try something new for me, this code will create a txt file on the desktop.
# You'll just answer the inputs, the code will add them to the list and at the and you'll have a to-do list on your desktop.

tasks = [] # This is our storage.

try:
    with open ("todo_list.txt", "r") as file: # We will make the list permament, so we will create a txt file later. But now, we must check if that file created before, so the PC could read it.
        for line in file:
          tasks.append(line.strip())
except FileNotFoundError: # That's for avoid having errors. Otherwise the proggram will keep failing because it won't be able to read the file.
    pass


print("Welcome to the To-Do List Maker!")



while True:
    print("You can do these three things; \n1-See the List\n2-Add a task\n3-Quit") 
    
    choice = input("What do you want to do? Write it as the line number as 1-2-3: ")
    
    if choice == "1": 
        if len(tasks) == 0: # We check this to avoid printing empty lists.
            print("Your list is empty, there's nothing to see.")
        else:
            n = 1
            for item in tasks:
                print(f"{n} - {item}") # I know we can do it with enumerate code, but I prefer to do it that way
                n += 1

    if choice == "2":
        new_task = input("Write the task: ") 
        tasks.append(new_task)
        with open("todo_list.txt", "a") as file: # Here create a todo_list.txt file
            file.write(new_task + "\n") # Then, we add new tasks to that list. 
        print("New task has succesfully added to your to-do list!")

    if choice == "3":
        print("Program is closing.")
        break
