
#json object to python object

# import json
# d='{"name":"abc"}'
# a=json.loads(d)
# print(type(a))


#python object to json object

# import json
# l=[1,2,3,4,5]
# a=json.dumps(l)
# print(type(a))

# import json
# t=(1,2,3,4,5)
# a=json.dumps(t)
# print(type(a))


import json
d={"name":"abc"}
a=json.dumps(d)
print(type(a))