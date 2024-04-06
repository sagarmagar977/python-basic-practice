print(''' 
################################################
######### BIKE RENTAL SYSTEM ###################
################################################
      ''')

class bikerental:
    def __init__(self,stock):
        
        self.stock=stock

    def displaystock(self):
        print(" number of bikes in stock : ",self.stock)
    def rentforbike(self,q):
        self.stock-=q
        if q<=0:
            print("enter the positive value or greater than zero !")
        elif q>=self.stock:
            print("enter value less than number of stock !!! ")
        else:
            print("totat rent = Rs",q*100)
            print("Reamaning stock =",self.stock)
while True:
    obj=bikerental(100)
    
    uc=int(input('''
    ENTER 1 to display stock !!!
    ENTER 2 to rent bike !!!
    ENTER 3 for exit |
    ---------> '''))

    if uc==1:
        obj.displaystock()
    elif uc==2:
       
        n=int(input("Enter number of bikes to rent = "))
         
        obj.rentforbike(n)
    else:
        break