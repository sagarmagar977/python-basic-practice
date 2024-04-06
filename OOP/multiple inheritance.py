####ISINGLE INHERiTANCE ####
class A:
    def displayA(self):
        print("helllo")
class B():
    def displayB(self):
        print("welcome") 
class C(A,B):
    def displayC(self):
        print("wscubetech")
obj=C()
obj.displayA()
obj.displayB() 
obj.displayC()   