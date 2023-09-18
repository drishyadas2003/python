# a=str(input("enter a string:"))
# v=['a','e','i','o','u']
# b=[]
# char=" "
# for i in a:
#     if i in v:
#         b.append(i)
# rev=b[::-1]
# l=list(a)
# l[1]=rev[0]
# l[-1]=rev[1]
# for i in l:
#     char+=i
# print(char)


a=str(input("enter a string:"))
v=['a','e','i','o','u']
b=[]
index=[]
ind=[]
char=" "
for i in a:
    if i in v:
        b.append(i)
        index=b.index(i)
        print(index)
rev=b[::-1]
for j in rev:
    ind=rev.index(j)
    print(ind)

# l=list(a)
# l[1]=rev[0]
# l[-1]=rev[1]
# for i in l:
#     char+=i
# print(char)

