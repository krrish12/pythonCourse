x="Hello | How are you | How u doing"

print("Expression value is: %c" %x[0])
#output: Expression value is: H

print("Expression value is: %s" %x[0:])
#output: Expression value is: Hello | How are you | How u doing

print("Expression value is: %s" %x[-1])
#output: Expression value is: g

print("Expression value is: %s" %x[0:-1])
#output: Expression value is: Hello | How are you | How u doin


print("Expression value is: %s" %x[0:5])
#output: Expression value is: Hello

print("Expression value is: %s" %x[:5])
#output: Expression value is: Hello

print("Expression value is: %s" %x.capitalize())
#output: Expression value is: Hello | how are you | how u doing

print("Expression value is: %s" %x.capitalize())
#output: Expression value is: Hello | how are you | how u doing

print("Expression value is: %s" %x.center(len(x)+2,'a'))
#output: Expression value is: aHello | how are you | how u doinga

print("Expression value is: %f" %x.count('doing'))
#output: Expression value is: 1.000000




