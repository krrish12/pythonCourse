var,var1 = 100,110
if ( var == 100 ) : print("Value of expression is 100 by Comparison operator")
#output: Value of expression is 100

if ( var == 10 ): print("Value of expression is 10 by Comparison operator")
elif(var1 == 50): print("Value of expression is 50 by Comparison operator")
else:print("Value of expression is 110 by Comparison operator")
#output: Value of expression is 100


if ( var or var1 ) : print("Result of expression is True by Logical operator")
#output: Result of expression is True by Logical operator

if ( var and var1 ) : print("Result of expression is False by Logical operator")
#output: Result of expression is False by Logical operator

if (not(var and var1)) : print("Result of expression is False by Logical operator")
else: print("Result of expression is True by Logical operator")
#output: Result of expression is True by Logical operator

if(var is 100): print("Value of expression is 100 by identity operator")
#output Value of expression is 100

if(var is not 100): print("Value of expression is 100 by identity operator")
else: print("Value of expression is 100 by identity operator by else ")
#output Value of expression is 100 by identity operator by else

obj,obj1 = 2,[1,2,10]

if(obj in obj1): print("Value of expression is 100 by membership operator")
#output Value of expression is 100 by membership operator

if(obj not in obj1): print("Value of expression is 100 by membership operator")
else :print("Value of expression is 100 by membership operator by else")
#output Value of expression is 100 by membership operator by else



