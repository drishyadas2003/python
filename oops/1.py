# class Person:
#     def sample(self):
#         print("hello")

#     def dis(self):
#         print("hai")

# ob=Person()
# ob.sample()
# ob.dis()
        



# class Person:
#     def add(self,a,b):
#         self.a=a
#         sum=a+b
#         print(sum)
#     def dis(self):
#         print(self.a)

# ob=Person()
# ob.add(1,6)
# ob.dis()
        


class Calculator:
    def add(self,a,b):
        self.a=a
        self.b=b
        sum=a+b
        print(sum)
    def sub(self):
        dif=self.a-self.b
        print(dif)
    def mul(self):
        mult=self.a*self.b
        print(mult)
    def div(self):
        dv=self.a/self.b
        print(dv)
ob=Calculator()
ob.add(12,6)
ob.sub()
ob.mul()        
ob.div()        



class Calculator:
    def add(self,a,b):
        self.a=a
        self.b=b
        sum=a+b
        print(sum)
    def sub(self):
        dif=self.a-self.b
        print(dif)
    def mul(self):
        mult=self.a*self.b
        print(mult)
    def div(self):
        dv=self.a/self.b
        print(dv)
v=int(input("::"))
m=int(input("::"))
ob=Calculator()
ob.add(v,m)
ob.sub()
ob.mul()        
ob.div()        




