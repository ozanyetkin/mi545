
# This is a comment, Python ignores this.

#%%
# __ : 'D'ouble + 'UNDER'score => DUNDER 

def add(x,y):
    'This is a thing that adds x and y.'
    print("Adding...")
    return x+y

print(add(3,3))

# %%
a = 5
b = a
b = b + 1

# %%
a = [1,2,3]
b = a
b[0] = b[0] + 1
# %%
myaddress = """
ODTU Enformatik Ens.
Dumlupınar Blv #1
Cankaya Ankara
"""
# %%
a = "aybar"
b = a
b = b + " acar"
# %%
def add_and_multiply(x, y):
    'Adds and multiplies x and y, returns the results, respectively'
    return ( x+y, x*y)
# %%


person = {   "name": "aybar",
            "lastname": "acar",
            "address": myaddress,
            "age": 42 ,
            34098: "mysecret",
            (1,4,5): 98 }
# %%


personlist = [ "aybar", "acar", myaddress, 42 ]
# %%
a = 5
a += 1 # == a = a + 1
a
# %%
s = 'sdfsdf'
s.upper()
# %%

data = [323, 234, 234, 22, 234 ,234 ,222,654, 234, 323]
j = 0
total = 0
while j < len(data) and data[j] != 'End':
    total += data[j]
    j += 1

print(total)
# %%
total = 0
for i in data:
    total += i
print(total)

#%%
for letter in s:
    print(letter)

#%%
for key in person:
    print(f"Your {key} is: {person[key]}")

# %%
n = 100
gauss = 0
for i in range(n):
    gauss += i

assert gauss == (n-1)*n/2 , f"the calculation was {gauss}, should have been {(n-1)*n/2}"
# %%

# %%

def hello(name='Stranger'):
    return f"Hello, {name}!"

# %%
def count(data, target): 
    n=0
    for item in data:
        if item == target:
            n += 1 
    return n
# %%

def contains(data, target):
    for item in data:
        if item == target:
            return True
# %%

def shoppinglist(**kwargs):
    print('Your shopping list is:')
    total = 0.0
    for item in kwargs:
        print(f"{item}: {kwargs[item]}TL")
        total += kwargs[item]
    print(f'Total: {total}₺')

# %%

def add(x=0, *args):
    result = x
    for arg in args:
        result += arg
    return result

# %%

import random
# %%
random.randint(0,10)
# %%

def dice(limit=None):
    if limit is  None:
        while True: 
            yield random.randint(1,6)
    else:
        for i in range(limit):
            yield random.randint(1,6) 

for die in dice(10):
    print(die)

d = dice(2)
try:
    while True:
        print(d.__next__())
except StopIteration:
    # Done
    pass

# %%

[(x,y) for x in range(4) for y in range(4) if x**2 + y**2 < 2]

# Equivalent 

coords = []
for x in range(4):
    for y in range(4):
        if x**2 + y**2 < 2:
            coords.append((x,y))

# %%

for x,y in [(x,y) for x in range(4) for y in range(4)]:
    print(f'{x}, {y}: {x-y}')

for t in [(x,y) for x in range(4) for y in range(4)]:
    print(f'{t[0]}, {t[1]}: {t[0]-t[1]}')

# %%
