max('Hello world')

for letter in 'Hello world':
    print(letter)

import math
math.sin(1)
degrees = 45
radians = degrees / 360.0 * 2 * math.pi
math.sin(radians)

import random
for i in range(10):
    x = random.random()
    print(x)

random.randint(5, 10)

t = [1,2,3]
for i in range(10):
    print(random.choice(t))


#testing if variables defined in functions are saved in the global environment
def test():
    a = 1
    b = 3
    print(a,b)

test()
a   #they are not

def addtwo(a,b):
    added = a + b
    return(added)
addtwo(5,4)

def computepay(rate, hours):
    if hours > 40:
        return(print('Pay: ', (hours - 40) * rate * 1.5 + 40 * rate)
    else:
        return(print('Pay: ', hours * rate))
