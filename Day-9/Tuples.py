tupObj1,tupObj2=(10,20),(30,40)

tupObj3 = tupObj1 + tupObj2

print("Expression value is:",tupObj3)
#output: Expression value is: (10, 20, 30, 40)

print("Expression value is:",tupObj3[:-1])
#output: Expression value is: (10, 20, 30)

print("Expression value is:",len(tupObj3))
#output: Expression value is: 4

print("Expression value is:",max(tupObj3))
#output: Expression value is: 40

print("Expression value is:",min(tupObj3))
#output: Expression value is: 10

print("Expression value is:",tuple(tupObj3))
#output: Expression value is: (10, 20, 30, 40)


            
