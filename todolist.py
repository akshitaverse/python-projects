tasks=[]
while True:
    print("***TO DO LIST***")
    print("1.add task")
    print("2.view tasks")
    print("3.remove task")
    print("4.exit")

    choices=int(input("ENTER YOUR CHOICE :"))
    
    if choices==1:
        while True:  
          task=input("enter task(type'done' to stop):")
          if task=="done":
           break

          tasks.append( task)

    elif choices==2:
        for i,task in enumerate(tasks,1):
             print(i,".",task)

    elif choices==3:
        task=(input("enter task to remove:"))   
        tasks.remove(task)

    elif choices==4:
        break

    else:
        print("INVALID CHOICE, TRY AGAIN!")     

