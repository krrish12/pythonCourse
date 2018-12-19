obj=10+4
print(obj)#int type
#output: 14

obj=10+3.0
print(obj)#float type
#output:13.0

obj=10-4
print(obj)#int type
#output: 6

obj=10-3.0
print(obj)#float type
#output:7.0

obj=2*2
print(obj)#int type
#output: 4

obj=4.0*2
print(obj)#float type
#output: 8.0

obj=2/2
print(obj)#float type
#output: 1.0

obj=2%2
print(obj)#int type
#output:0

obj=2%2.0
print(obj)#float type
#output: 0.0

obj=2.0%2
print(obj)#float type
#output: 0.0

obj=10+4j
print(obj)#complex type
#output:(10+4j)

obj = 2**3
print(obj)#int type
#output: 8

obj = 3//2
print(obj)#int type
#output: 1

obj = 3//2.0
print(obj)#float type
#output: 1.0

#Comparison Operators

obj,obj1 = 2,3

print(obj == obj1)#boolean type
#output: False

print(obj is obj1)
#output: False

print(obj != obj1)
#output: True

print(not(obj == obj1))
#output: True

print(not(obj != obj1))
#output: False

print(obj > obj1)
#output: False

print(obj < obj1)
#output: False

print(obj >= obj1)
#output: True

print(obj <= obj1)
#output: False

#Logical Operators

print(obj and obj1)
#output: 3

print(obj or obj1)
#output: 2

#Bitwise Operators
print(obj & obj1)
#output: 2

print(obj | obj1)
#output: 3

print(~obj)
#output: -3

print(obj ^ obj1)
#output: 1

print(obj>> 2)
#output: 0

print(obj << 5)
#output: 64

#Identity Operators

print(obj is not obj1)
#output: True

print(obj is obj1)
#output: False

#Membership Operators
a,b = 2,[1,2,3]
print(a in b)
#output: True

print(a not in b)
#output: False

