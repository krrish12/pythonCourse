dicObj={'key1':10,'key2':20 , 'key3':30,'key4':40}

print("Expression value is:",dicObj)
#output: Expression value is: {'key1': 10, 'key2': 20, 'key3': 30, 'key4': 40}

print("Expression value is:",dicObj.keys())
#output: Expression value is: dict_keys(['key1', 'key2', 'key3', 'key4'])

print("Expression value is:",dicObj.values())
#output: Expression value is: dict_values([10, 20, 30, 40])

print("Expression value is:",dicObj['key2'])
#output: Expression value is: 20

dicObj['key2'] = '25'
print("Expression value is:",dicObj)
#output: Expression value is: {'key1': 10, 'key2': '25', 'key3': 30, 'key4': 40}

del dicObj['key2']
print("Expression value is:",dicObj)
#output: Expression value is: {'key1': 10, 'key3': 30, 'key4': 40}

dicObj['key2'] = '20'
print("Expression value is:",dicObj)
#output: Expression value is: {'key1': 10, 'key2': '20', 'key3': 30, 'key4': 40}


print("Expression value is:",len(dicObj))
#output: Expression value is: 4

print("Expression value is:",str(dicObj))
#output: Expression value is: {'key1': 10, 'key3': 30, 'key4': 40, 'key2': '20'}

print("Expression value is:",type(dicObj))
#output: Expression value is: <class 'dict'>

