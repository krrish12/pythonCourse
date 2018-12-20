a,b=[10,20],[30,40]

print("Expression value is:",len(a))
#output: Expression value is: 2

print("Expression value is:",max(a))
#output: Expression value is: 20

print("Expression value is:",min(a))
#output: Expression value is: 10

obj=(10,20,30)
print("Expression value is:",list(obj))
#output: Expression value is: [10, 20, 30]

a.append(30)
print("Expression value is:",a)
#output: Expression value is: [10, 20, 30]

print("Expression value is:",a.count('30'))
#output: Expression value is: 0

print("Expression value is:",a.count(30))
#output: Expression value is: 1

a.extend(b)
print("Extended List : ", a)
#output: Extended List :  [10, 20, 30, 30, 40]

print("Expression value is:",a.index(30))
#output: Expression value is: 2

a.insert(3,35)
print("Expression value is:",a)
#output: Expression value is: [10, 20, 30, 35, 30, 40]

a.pop()
print("Expression value is:",a)
#output: Expression value is: [10, 20, 30, 35, 30]

a.remove(30)
print("Expression value is:",a)
#output: Expression value is: [10, 20, 35, 30]

a.reverse()
print("Expression value is:",a)
#output: Expression value is: [30, 35, 20, 10]

a.sort(reverse=True)
print("Expression value is:",a)
#output: Expression value is: [35, 30, 20, 10]
