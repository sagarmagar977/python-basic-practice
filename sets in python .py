 ################################################################
##### SETS IN PYTHON ######
# it is defined by curly brackets = {}
# set stores unique values
# set is unordered and unindex data type
# its elements  can be deleted , and new elements can be added but elements can not be replaced and modified

## example :
"""
s={10,20,30}
for a in s:
    print(a)

"""

## FUNCTIONS USED INSIDE SETS ##
# set() = this function converts list into sets
# add() = add new elment to the set
# pop() = pop a random element 
# remove() = remeove a paraticular elemtn put inside parenthesis
# clear() = clear all elements from set
# discard9 = discard a particular element from set
# update() = update a set with new elements

## example :
# use of set() function :
'''
l=[0,20,30,40,50]
s=set(l)
print(s)

'''

## use of add() function :
"""
s={10,20,30,50}
s.add(70)
print(s)

"""

## use of pop() function :
"""
#it pops random element

s={10,20,30,50}
b=s.pop()
print(b)
print(s)

"""

## use of  remove() function :
"""

s={10,20,30,50}
s.remove(50)
print(s)

"""

## use of clear() function :
"""
#its clear out all elements from set
s={10,20,30,50}
s.clear()
print(s)

"""

## use of discard() function :
"""
s={10,20,30,50}
s.discard(20)
print(s)

"""

## use of update function () :

s={10,20,30,50}
l={10,70,80,90}
s.update(l)
print(s)









 
