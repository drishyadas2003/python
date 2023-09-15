

# s=open("sample.txt","w")
# s.write("Hello")
# s.close()


# s=open("sample.txt","w")
# s.write("Hello\n")
# s.write("Hello\n")
# s.write("Hello\n")
# s.write("Hello\n")
# s.write("Hello\n")
# s.close()

# s=open("sample.txt","r")
# print(s.read())


# import os 
# old="sample.txt"
# new="demo.html"
# os.rename(old,new)
 
# os.remove("demo.html")


# import os
# import shutil
# src=r"c:\Users\software-4pm\Downloads\sample.txt"
# des=r"c:\Users\software-4pm\Documents"
# shutil.move(src,des)


import os
import shutil
src=r"c:\Users\software-4pm\Downloads\text.txt"
des=r"c:\Users\software-4pm\Documents"
shutil.copy(src,des)