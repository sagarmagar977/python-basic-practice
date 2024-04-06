

# THIS WILL SHOW ERROR AS THE __ name variable is private
"""

class student:
    __name="Ravi"
obj=student()
print(obj.__name)

"""

## private varibale can only be used inside the class

class student:
    __name="Ravi"
    def __init__(self):
        print(self.__name)
obj=student()
#print(obj.__name)

