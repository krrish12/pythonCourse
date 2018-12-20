listObj,listObj1=[10,20],[30,40]

print("Expression value is:",len(listObj))
#output: Expression value is: 2

print("Expression value is:",max(listObj))
#output: Expression value is: 20

print("Expression value is:",min(listObj))
#output: Expression value is: 10

obj=(10,20,30)
print("Expression value is:",list(obj))
#output: Expression value is: [10, 20, 30]

listObj.append(30)
print("Expression value is:",listObj)
#output: Expression value is: [10, 20, 30]

print("Expression value is:",listObj.count('30'))
#output: Expression value is: 0

print("Expression value is:",listObj.count(30))
#output: Expression value is: 1

listObj.extend(listObj1)
print("Extended List : ", listObj)
#output: Extended List :  [10, 20, 30, 30, 40]

print("Expression value is:",listObj.index(30))
#output: Expression value is: 2

listObj.insert(3,35)
print("Expression value is:",listObj)
#output: Expression value is: [10, 20, 30, 35, 30, 40]

listObj.pop()
print("Expression value is:",listObj)
#output: Expression value is: [10, 20, 30, 35, 30]

listObj.remove(30)
print("Expression value is:",listObj)
#output: Expression value is: [10, 20, 35, 30]

listObj.reverse()
print("Expression value is:",listObj)
#output: Expression value is: [30, 35, 20, 10]

listObj.sort(reverse=True)
print("Expression value is:",listObj)
#output: Expression value is: [35, 30, 20, 10]

print("Expression value is:",type(listObj))
#output: Expression value is: <class 'list'>
