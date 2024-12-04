Tasks=[]
print("welcome user!\n\n\n To Add Tasks Type A: \n To see your Tasks Type B:  \n To Exit Type E : \n\n\n")

while True:

    a= input("The Letter:\n")

    if a =="A" or a=="a":
        task=input("Enter your tasks: \n")
        Tasks.append(task)
        print(f"Task sucessfully saved\n")
        while True:
         new_task=input("Do you wish to add another task? Y/N:\n")
         if new_task=="Y" or new_task=="y":
             task=input("Enter your tasks:\n")
             Tasks.append(task)
         else:
             break
             

    elif a=="B" or a=="b":
        i=1
        print("Here are all the tasks that you have got:\n")

        for task in Tasks:
            
            print(f"{i}.{task}")
            i=i+1
        
        a=int(input("put the numerical value for the task that is completed,example=1: \n\n"))
        n=(a-1)
        if 0 <=n:
            Tasks.pop(n)
            i=1
            for task in Tasks:
                
                print(f"{i}.{task}")
                i=i+1
            print("\nGreat Job\n")

    elif a=="E" or a=="e":
        print("You did great today")
        break
    
    else:
        print("Rerun the program")
        break