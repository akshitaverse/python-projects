import random
import string
 
letters=string.ascii_letters
numbers=string.digits
symbols=string.punctuation

characters=letters

choice1=input("include numbers?(y/n):")
if choice1.lower()=="y":
    characters+=numbers

choice2=input("include symbols?(y/n):")
if choice2.lower()=="y":
    characters+=symbols

length=int(input("ENTER PASSWORD LENGTH:"))
password=""
for i in range(length):
    password+=random.choice(characters)

print("YOUR PASSWORD IS",password)


