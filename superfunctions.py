#fiter()

# def dis(n):
#     return n%2==0
# s=filter(dis,[1,2,3,4,5,6])
# print(list(s))


# def dis(n):
#     return n%3==0
# a=filter(dis,[1,22,55,9,12])
# print(list(a))

#map()

# def dis(n):
#     return n*3
# a=map(dis,[1,2,3,4,5,6])
# print(list(a))


# def dis(a,b):
#     return a+b
# n=map(dis,[1,2,3,4,5,6],[7,8,9,10,11,12])
# print(list(n))


# c=map(lambda n:n*3,[1,2,3,4])
# print(list(c))





# def dis(n):
#     return "a" in n
# s=filter(dis,("apple","orange","xyz"))
# print(list(s))



# c=filter(lambda n:"a" in n,("apple","orange","xyz"))
# print(list(c))

#reduce()

# from functools import reduce

# def dis(a,b):
#     return a+b
# s=reduce(dis,range(1,6))
# print(s)

# from functools import reduce

# c=reduce(lambda a,b:a+b,range(1,6))
# print(c)


def dis(n):
    return n%2==0
    
s=filter(dis,[66,18,22,55,9,12])

from functools import reduce
def sum(a,b):
    return a+b
c=reduce(sum,s)
print(c)