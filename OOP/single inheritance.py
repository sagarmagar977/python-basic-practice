####ISINGLE INHERiTANCE ####
class A:
    def displayA(self):
        print("helllo")
class B(A):
    def displayB(self):
        print("welcome")   
obj=B()
obj.displayA()
obj.displayB()  