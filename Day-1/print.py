#python version 3
#print string,int,float
print("Hello world")
#output: Hello world

print(1)
#output: 1

print(2.0)
#output: 2.0

obj,obj1 = 2,3
print(obj,",",obj1)
#output: 2 , 3

obj=obj1=obj2=10
print(obj,",",obj1,",",obj2)
#output: 10 , 10 , 10

#Arrays
obj=["Hello",1254,2.0]
print(obj)
#output: ('Hello', 1254, 2.0)

print(obj[2])
#output:2.0

print(obj[2:])
#output:[2.0]

#tuple
obj=("Hello",1254,2.0)
print(obj)
#output: ('Hello', 1254, 2.0)

print(obj[0])
#output: Hello

print(obj * 2)
#output: ('Hello', 1254, 2.0, 'Hello', 1254, 2.0)

#Dictionary
obj={}
obj = {'name':'Mickey'}
print(obj)
#output: {'name' : 'Mickey'}

print(obj.keys())
#output: dict_keys(['name'])

print(obj.values())
#output: dict_values(['Mickey'])

print(obj['name'])
#output: Mickey

