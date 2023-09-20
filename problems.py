# # a=str(input("enter a string:"))
# # v=['a','e','i','o','u']
# # b=[]
# # char=" "
# # for i in a:
# #     if i in v:
# #         b.append(i)
# # rev=b[::-1]
# # l=list(a)
# # l[1]=rev[0]
# # l[-1]=rev[1]
# # for i in l:
# #     char+=i
# # print(char)


a=str(input("enter a string:"))
v=['a','e','i','o','u']
b=[]
index=[]
ind=[]
count=0
c=0
l1=[]
l2=[]
char=" "
for i in a:
    if i in v:
        b.append(i)
        index=b.index(i)
        l1.append(index)
        count+=1
        l2.append(count)
print(l1)
print(l2)
        
# # rev=b[::-1]
# # for j in rev:
# #     ind=rev.index(j)
# #     c+=1
# #     l2.append(c)
# # print(l2)
# # l=list(a)


# # l=list(a)
# # l[1]=rev[0]
# # l[-1]=rev[1]
# # for i in l:
# #     char+=i
# # print(char)





# # a=int(input("enter a number:"))
# # b=str(a)
# # print(b[::-1])

