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
#output: Expression value is: Hello | How are you | How u doing

print("Expression value is: %s" %x[::-1])#syntax: start:stop:step
#output: Expression value is: gniod u woh | uoy era woh | olleH

print("Expression value is: %s" %x.capitalize())
#output: Expression value is: Hello | how are you | how u doing

print("Expression value is: %s" %x.capitalize())
#output: Expression value is: Hello | how are you | how u doing

print("Expression value is: %s" %x.center(len(x)+2,'a'))#syntax: width, fillchar
#output: Expression value is: aHello | how are you | how u doinga

print("Expression value is: %f" %x.count('doing'))
#output: Expression value is: 1.000000

print(x.endswith('doing'))
#output: True

print(x.endswith('ow',8,11))#syntax: suffix, start, end
#output: True

y="Hello\t|How are you|How u doing"
print(y.expandtabs(1))
#output: "Hello |How are you|How u doing"

print(x.find('|'))
#output 6

print(x.index("|",7,len(x)))
#output 20 second occurence of |

y="abc123"
print(y.isalnum())
#output True

y="abc!"
print(y.isalnum())
#output False

