# class A:
#     def __init__(self,n,m):
#         self.num1=n
#         self.num2=m
#     def add(self):
#         print(self.num1+self.num2)
# ob=A(10,20)
# ob.add()
        

#single inheritance
# class A:
#     def dis(self):
#         print("hai")
# class B(A):
#     pass
# ob=B()
# ob.dis()


# #multiple inheritance
# class A:
#     def dis(self):
#         print("hai")
# class B:
#     def display(self):
#         print(10)
# class C(A,B):
#     pass
# ob=C()
# ob.dis()
# ob.display()


#multi level inheritance
# class A:
#     def dis(self):
#         print("hai")
# class B(A):
#     def display(self):
#          print(10)
# class C(B):
#     def d(self):pass
#         print(5)
# class D(C):
#     pass
# ob=D()
# ob.dis()
# ob.display()
# ob.d()


# class Vehicle:
#     def start_engine(self):
#         print("the engine is starting")
# class Car(Vehicle):
#     def drive(self):
#         print("the car is driving")
# ob=Car()
# ob.start_engine()
# ob.drive()


# class Employee:
#     def dis(self,name,salary):
#        self.name=name
#        self.salary=salary
#        print(self.name,self.salary)
# class Manager(Employee):
#     def display(self,department):
#         self.department=department
#         print(self.department)
# ob=Manager()
# ob.dis("drishya",15000)
# ob.display("sales")


# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def p(self):
#         print(self.name,self.age)
# class Employee(Person):
#     def __init__(self, salary):
#         self.salary=salary
#     def e(self):class A:
#     def dis(self):
#         print("hai")
# class B(A):
#     pass
# ob=B()
# ob.dis()


# ob=Manager("sales")
# obj=Employee(1500000)
# obje=Person("drishya",20)class A:
#     def dis(self):
#         print("hai")
# class B(A):
#     pass
# ob=B()
# ob.dis()




# class A:
#     def sample(self):
#         print("hello")
# class B(A):
#     pass
# class C(A):
#     pass
# class D(A):
#     pass
# o=B()
# o.sample()
# ob=C()
# ob.sample()
# obj=D()
# obj.sample()




# class Person:
#     def speak(self,name,age):
#         self.name=name
#         self.age=age
#         print(self.name,"is speaking")
# class Student(Person):
#     def study(self):
#         print("hai")
# class Teacher(Person):
#     def teach(self):
#         print("hello")
# ob=Student()
# ob.speak("drishya",20)
# ob.study()
# obj=Teacher()
# obj.speak("drishya",20)
# obj.teach()



# class A:
#     def dis(self):
#          print("hai")
# class B(A):
#      def b(self):
#           print("hello")
# class C(A):
#      def c(self):
#           print("python")
# class D(A):
#     def d(self):
#          print("drishya") 
# ob=B()
# ob.dis()
# ob.b()
# obj=C()
# obj.dis()
# obj.c()
# obje=D()
# obje.dis()
# obje.d()


class A:
    def dis(self):
         print("hai")
class Parent:
     def parent(self):
          print("parent")
class B(A,Parent):
     def b(self):
          print("hello")
class C(A):
     def c(self):
          print("python")
class D(A):
    def d(self):
         print("drishya") 

ob=B()
ob.dis()
ob.parent()
obj=C()
obj.dis()
obj.c()

