####ISINGLE INHERiTANCE ####
class A:
    def displayA(self):
        print("helllo")
class B(A):
    def displayB(self):
        print("welcome") 
class C(B):
    def displayC(self):
        print("wscubetech")
obj=C()
obj.displayA()
obj.displayB() 
obj.displayC() 