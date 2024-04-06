 ####USE AOF SELF #####
class DemoClass:
    a=10
    b=20
    def showvalue(self):
        self.c=self.a*self.b
        print(self.c)
    def showinfo(self):
        print("welcome python lovers !!")
    def sum(self,a,b):
            print(a+b)
    def __init__(self):
         print("hello")         
obj=DemoClass()
obj.showvalue()
obj.showinfo()
obj.sum(40,50)
 