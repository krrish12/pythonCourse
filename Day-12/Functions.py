sum = lambda arg1,arg2:arg1+arg2;#single line function
print(sum(10,20))
#output: 30

def Hello():
  print("Welcome")
Hello()

#output: Welcome

total=0
def Demo(arg1,arg2):
    total = arg1 + arg2
    print("inside",total)

Demo(10,20)
print("outside:",total)

#output: inside 30
        #outside 0
    
total = 0
def Demo(arg1,arg2):
    global total
    total = arg1 + arg2
    print("inside",total)
    return;

Demo(10,20)
print("outside:",total)
#output: inside 30
        #outside 30
