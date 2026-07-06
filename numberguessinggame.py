#number guessing game
import random
computer=random.randint(1,100)
attempts=0
while True:
 user=int(input("guess a number & enter the number you guessed:"))
 attempts+=1
 if computer==user:
    print(" FINALLY YOU GUESSED IT!!!")
    
    print("attempts:",attempts)
    break
 elif computer>user:
    print("TOO LOW!")
 else :
    print("TOO HIGH!")   
print("the number was:",computer)    

