print("~~~WELCOME TO THE QUIZ~~~")
SCORE=0

print("1. What is the capital of india?")
ans=input("answer:")
if ans=="delhi" or ans=="Delhi":
    print("CORRECT!")
    SCORE+=1
else:
    print("WRONG!")

print("2. which keyword is used to define a function in python?")
ans2=input("answer:")
if ans2=="def" or ans2=="Def":
    print("CORRECT")
    print("GOOD")
    SCORE+=1
else:
    print("WRONG!")

print("3.which data type stores true/false")
ans3=input("answer:")
if ans3=="bool" or ans3=="Bool":
    print("Correct")
    SCORE+=1
else:
    print("WRONG!")    

print("who developed python?")
ans4=input("answer:")
if ans4=="Guido van Rossum" or ans4=="Guido" or ans4=="guido" or ans4=="guido vanrossum":
    print("CORRECT!")
    SCORE+=1
else:
    print("WRONG!!") 

print("5.which loop repeats until a condition becomes false?")
ans5=input("answer:")
if ans5=="While" or ans5=="while":
    print("CORRECT!")
    SCORE+=1
else:
    print("WRONG")     

print("your score=", SCORE)
if SCORE==5:
    print("EXCELLENT!!!")
elif SCORE==4 or SCORE==3:
    print("GOOD JOB!")
else:
    print("KEEP PRACTICING!")    
    



