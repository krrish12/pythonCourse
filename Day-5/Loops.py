count = 0
while count < 2:
   print(count, " is  less than 2")
   count = count + 1
else:
   print(count, " is not less than 2")

#output:
   # 0 is less than 2
   # 1 is less than 2
   # 2 is not less than 2

for letter in 'Python':     # First Example
   print('Current Letter: %c' % letter)
else:
    print("The End")

#output:
   #Current Letter: P
   #Current Letter: y
   #Current Letter: t
   #Current Letter: h
   #Current Letter: o
   #Current Letter: n
   #The End

for num in range(10,15):
    print('%d' % num)
else:
    print('%d' % (num+1))

#output:
    #10
    #11
    #12
    #13
    #14
    #15
for num in range(10,15):
    print('%f' % num)

#output:
    #10.000000
    #11.000000
    #12.000000
    #13.000000
    #14.000000
            

