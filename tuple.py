###########################################################################
#### TUPLE #####
#tuple is an ordered data type 
#it is used with "()" parenthesis
#It is imutable , i.e. it can not be modified.
# a single element in tuple can not be called tuple.
#for example :
''' 
a=(5)
print(type(a)) 
''' 
''' 
a=("hello")
print(type(a))
''' 

#### ITERATION OF TUPLE  USING FOR LOOP ####


"""

t=(3,5,4,6,7,8)
l=len(t)
for a in range(l):
    print(a)
    print(t[a])
"""

#### FUNCTIONS USED INSDIE TUPLE ######
"""
min() = returns minimum value
max() = returns maximum value
count() = count the repeated number of any value inside parametr
index() = returns index number of any value
sum() = return sum of all values of tuple if elements are intigers

"""    

## example :

"""
a=(3,4,5,6,7,8,9)
b=min(a)
c=max(a)
d=a.count(4)
e=a.index(6)
f=sum(a)

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

"""


### TUPLE SUM ###


t=(2,3,4,5,6,7,8,9)
S=sum(t)
q=sum(t,10)
print(S)
print(q)

####################################################################################





