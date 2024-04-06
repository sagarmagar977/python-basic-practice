######## GUESS THE NUMBER QUIZ #######
import random
cnum=random.randrange(1,101)
usernum=int(input("Enter your guess number : "))
print("computer's guess : ", cnum)
if cnum==usernum:
    print(" your guess is right")
elif cnum>usernum:
    print(" your guess is  low ! ")
else :
     print(" your guess is high")    