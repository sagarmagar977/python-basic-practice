######################################
##### USER DEFINED FUNCTIONS ########
# USER-DEFINED FUNCTIONS ARE OF THREE TYPES 
#   1) simple function
#   2) function with argument
#   3) function with return value


###### 1) SIMPLE FUNCTION #######
'''

def simpleFunction():
     print("welcome to VS code")
simpleFunction()

'''

###### 2) FUNCTION WITH ARGUMENT ######
 
#using two argument with no default value
'''
def sum(a,b):
    print(a+b)
n1=10
n2=20
m1=30
m2=40
sum(n1,n2)
sum(m1,m2)

'''
#using two argument with one default value :
'''
def sum(a,b=8):
    print(a+b)
n1=10
n2=20
m1=30
m2=40
sum(n1,n2) 
sum(n1) #when one argument given then second value will be deafault value of b
sum(n2) 
sum(m1,m2)

'''

##### 3) FUNCTION WITH RETURN VALUE ######
# -- This type of function is create to store the value , it can not to print the value

'''

def sum(a,b):
    c=a+b
    return c
sum(8,9)

'''
# To print we must change a code little bit 

'''

def sum(a,b):
     c=a+b
     return c
d=sum(8,9)
print(d)

'''










