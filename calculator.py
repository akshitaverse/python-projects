def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b

while True:
    
    choice=int(input("enter 1 for add ,2 for subtract,3 for multiply,:4 for divide &5 for exit:"))
    if choice==5:
        print("BYE BYE!")
        break
    num1=int(input("enter 1st number:"))
    num2=int(input("enter 2nd number:"))
    if choice==1:
        print(add(num1,num2))
    elif choice==2:
        print(subtract(num1,num2))
    elif choice==3:
        print(multiply(num1,num2))
    elif choice==4:
        if num2==0:
            print("cannot divide by zero!!!")
        else:    
            print(divide(num1,num2))
    
    else:
        print("INVALID CHOICE!")



