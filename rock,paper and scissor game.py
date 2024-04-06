####### ROCK , PAPER AND SCISSOR GAMME ##############
import random
L=["ROCK","PAPER","SCISSOR"]

c_count=0
u_count=0
print("#################  ROCK ,PAPER AND SCISSOR MATCH #################")
while True:
    u_demand=int(input(''' 
                       ENTER | 1 |  to PLAY !
                       ENTER | 2 |  to exit !

            ---------------> ''' ))
    if u_demand==1:
        print("lets play")
        for a in range(1,6):
             u_c=int(input( """
                        enter :
                        1 for ROCK
                        2 for PAPER
                        3 for SCISSOR
                           
                   ----> """))
             
             if u_c==1 :
              u_c="ROCK"
              print("#################")
              print("You choose  : ROCK")
             elif u_c==2:
                 u_c="PAPER"
                 print("#################")
                 print("You choose  : PAPER")
             elif u_c==3:
                u_c="SCISSOR"
                print("#################")
                print("You choose :  SCISSOR")

             c_c=random.choice(L)
             print("#################")
             print( "computer choose : ", c_c)




             if u_c==c_c:
                 print("#################")
                 print("It is draw")
                 c_count+=1
                 u_count+=1
             elif (u_c=="ROCK" and c_c=="SCISSOR") or (u_c=="PAPER" and c_c=="ROCK")  or  (u_c=="SCISSOR" and c_c=="PAPER"):
                print("#################")
                print("you won !!!")
                u_count+=1
             else :
                 print("#################")
                 print("computer won !!! ")
                 c_count+=1
        print("#################")
        print("#################")
        print("Match is over!!!")
        print("#################")
        print("#################")
        print("Computer's score = ", c_count)
        print("    Your's score = ", u_count)  
        print("#################") 
        if c_count>u_count:
            print("Computer won !!!!")  
            print("#################") 
        else :
            print("you won !!!!!!")    
            print("#################")











    else :
          break
