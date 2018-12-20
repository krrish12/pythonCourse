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

print("Expression value is:",x.startswith('ow',8,11))#syntax: suffix, start, end
#output: Expression value is: False

print("Expression value is:",x.startswith('ow',9,11))#syntax: suffix, start, end
#output: Expression value is: True

y="Hello\t|How are you|How u doing"
print(y.expandtabs(1))
#output: "Hello |How are you|How u doing"

print(x.find('|'))
#output: 6

print(x.index("|",7,len(x)))#syntax string,begin index,end index
#output: 20 second occurence of |

y="abc123"
print(y.isalnum())
#output: True

y="abc!"
print(y.isalnum())
#output: False

print("isAlpha:",y.isalpha())
#output: isAlpha: False

print("isDigit:",y.isdigit())
#output: isDigit: False

y="1234"
print("isDigit:",y.isdigit())
#output: isDigit: True

print("isLower:",x.islower())
#output: isLower: False

print("isUpper:",x.isupper())
#output: isUpper: False

print("isNumeric:",y.isnumeric())
#output: isNumeric: True

print("isSpace:",x.isspace())
#output: isSpace: False

z="     "
print("isSpace:",z.isspace())
#output: isSpace: True

print("isTitle:",x.istitle())
#output: isTitle: False

abc="Hello How"
print("isTitle:",abc.istitle())
#output: isTitle: True

a,b,c="-",["d","e","f"],"Hello"
print(a.join(b))
#output: d-e-f

print("Lenth of a: %d" %len(a))
#output: Lenth of a: 1

print("Lenth of c: %d" %len(c))
#output: Lenth of c: 5

print("Expression value is: %s" %c.ljust(len(c)+2,'!'))#syntax: width, fillchar
#output: Expression value is: Hello!!

print("Expression value is: %s" %c.rjust(len(c)+2,'!'))#syntax: width, fillchar
#output: Expression value is: !!Hello

print("Expression value in lower case is: %s" %c.lower())
#output: Expression value in lower case is: hello

c="  Hello  "
print("Expression value after removes leading whitespace is: %s" %c.lstrip())
#output: Expression value after removes leading whitespace is: Hello

print("Expression value after removes trailing whitespace is: %s" %c.rstrip())
#output: Expression value after removes trailing whitespace is:    Hello

intab = "Hy|gd"
outtab = "62345"
trantab = x.maketrans(intab, outtab)
print("Expression value is: %s" %x.translate(trantab))
#output: Expression value is: 6ello 3 6ow are 2ou 3 6ow u 5oin4

print("Maximum value in string is: %s" %max(x))
#output: Maximum value in string is: |

lst=[10,20,30,40,50]
print("Maximum value in string is: %f" %max(lst))
#output: Maximum value in string is: 50.000000

print("Minimum value in string is: %d" %min(lst))
#output: Minimum value in string is: 10

print("Expression value is: %s" %x.replace("How","why"))
#output: Expression value is: Hello | why are you | why u doing

print("Expression value is: %s" %x.replace("How","why",1))#syntax: old, new, occurence
#output: Expression value is: Hello | why are you | How u doing

print("Expression value is: %d"%x.rfind("|"))
#output: Expression value is: 20

print("Expression value is: %d"%x.rindex("How"))
#output: Expression value is: 22

print("Expression value is:",x.split("|"))
#output: Expression value is: ['Hello ', ' How are you ', ' How u doing']

print("Expression value is:",x.split("|",1))#syntax string, number of occurence
#output: Expression value is: ['Hello ', ' How are you ', ' How u doing']

obj="He\nllo"
print("Expression value is:",obj.splitlines())
#output: Expression value is: ['He', 'llo']

print("Expression value is:",obj.splitlines(obj.count("l")))
#output: Expression value is: ['He\n', 'llo']

obj="Hello"
print("Expression is:",obj.strip("o"))
#output: Expression is: Hell

obj="   Hello    "
print("Expression is:",obj.strip())
#output: Expression is: Hello


obj="hElP"
print("Expression is: %s" %obj.swapcase())
#output:Expression is: HeLp

obj="HELP"
print("Expression is: %s" %obj.swapcase())
#output:Expression is: help

obj="help"
print("Expression is: %s" %obj.swapcase())
#output:Expression is: HELP

obj="hElp"
print("Expression is: %s" %obj.title())
#output:Expression is: Help

obj="hElp"
print("Expression is: %s" %obj.zfill(len(obj)+2))
#output:Expression is: 00hElp

decimal=u"2345"
print("Expression is:",decimal.isdecimal())
#output: Expression is: True

decimal=u"a2345"
print("Expression is:",decimal.isdecimal())
#output: Expression is: False

