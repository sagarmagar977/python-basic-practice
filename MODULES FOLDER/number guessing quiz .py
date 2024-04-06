##### NUMBER GUESSING QUIZ #####
import random
cnum=random.randrange(1,101)
usernum=int(input("guess number between 1 to 100 : "))
print("your number = ",usernum)
print("compute number = ", cnum)
if usernum>100:
    print("invalid guess !!!")
elif usernum==cnum:
    print("correct guess")
elif usernum>cnum+1:
    print("slightly high")
elif usernum<cnum-1:
    print("slight low")
elif usernum>cnum:
    print("guess to high") 
elif usernum<cnum:
    print(" guess too low")   
elif usernum>100 :
    print("invalid guess")
            