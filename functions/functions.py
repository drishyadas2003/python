# def sample():
#     print("hello")
# sample()


# def sample():
#     print("hello")
# a=int(input(":"))
# if a==1:
#     sample()
# else:
#     pass


#functions with arguments


# def sample(a,b):
#      print(a+b)
# sample(10,20)


# def sample(a,b):
#      print(a+b)

# x=int(input("first no:"))
# y=int(input("second no:"))
# sample(x,y)


# def add(a,b):
#      print(a+b)
# def mul(a,b):
#      print(a*b)
# def sub(a,b):
#      print(a-b)
# def div(a,b):
#      print(a/b)

# x=int(input("first no:"))
# y=int(input("second no:"))
# user=input("which one?")
# if user=="add":
#      add(x,y)
# elif user=="sub":
#      sub(x,y)
# elif user=="mul":
#      mul(x,y)
# else:
#      div(x,y)


# def remove_duplicate(lst):
#      l=[]
#      for i in lst:
#         if i not in l:
#             l.append(i)
#      print(l)
# l1=[1,2,3,2,2,1,4,5,3]
# remove_duplicate(l1)


# def sum_of_squares(n):
#      sum=0
#      for i in range(1,n+1):
#         sq=i**2
#         print(sq)
#         sum+=sq
#      print("sum of squares:",sum)
# a=int(input("enter a number:"))
# sum_of_squares(a)


# def filter_even_numbers(lst):
#      l=[]
#      for i in lst:
#           if i%2==0:
#                l.append(i)
#      print(l)
# l1=[1,2,3,4,5,6,7,8,9,10]
# filter_even_numbers(l1)



# def is_valid_email(email):
#      if "@" in email and "." in email:
#         print("True")
#      else:
#         print("False")
# email=input("enter your email:")
# is_valid_email(email)



#return function 

# def sample(a,b):
#     return a+b
# print(sample(10,20))


def are_anagrams(str1,str2):
    a=str(str1)
    b=str(str2)
    for i in a:
        if i in b:
            return True
        return False

           
a=str(input("enter a string:"))
b=str(input("enter a string:"))
print(are_anagrams(a,b))
