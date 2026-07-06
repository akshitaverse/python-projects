import random
def checkwin(user,c):
    if user==c:
        return "draw"
    elif (user=='s' and c=='w')or(user=='w' and c=='g')or(user=='g' and c=='s'):
        return "YOU WIN"
    else:
        return "COMPUTER WINS"
    
choices=['s','w','g']
c=random.choice(choices)

user=input("enter s for snal=ke, w for water and g for gun:")
if user not in choices:
    print("INVAlID INPUT")
else:    
  print("computer chose:",c)
  result=checkwin(user,c)
  print(result)    
  