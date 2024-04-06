####INCAPSULATION#####
class student:
    def __init__(self):
          self.__name=""
    def getname(self):
         return self.__name
    def setname(self,name):
         self.__name=name
obj=student()
obj.setname("RAMESH")
x=obj.getname()
print(x)