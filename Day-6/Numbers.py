x=5
print(int(x))
#output: 5

print(float(x))
#output: 5.0

print(complex(x))
#output: (5+0j)

print(complex(x,9))
#output: (5+9j)

#Random Number Functions

import random
x =[10,20,30,40,50]
print("random: %f" %random.choice(x))
#ouput: random: 50.000000

print("random: %d" %random.randrange(10,40,2))
#output: random: 34

print("random:",random.random())
#output: random: 0.428

random.seed(2)
print("seed random:",random.random())
#output: seed random: 0.95

random.shuffle(x)
print("random shuffle:",x)
#output: random shuffle: [30, 20, 40, 50, 10]

print("random uniform: %d" %random.uniform(2,5))
#output: random uniform: 4
