import random

a=random.randint(1,10)  #Returns a random interger with both includes
print(a)

print(random.random()) # returns a float num beteen 1 and 0

b=random.uniform(1,10) #Returns a random float numbers from attribue a and b
print(b)

# Choosing Random Elements

li=["Muni","Apple","Mango","Grapes"]
mn=random.choice(li) #Picks a random item from a list, tuple, or string.
print(mn)

mo=random.sample(li,2) #Pick two unique numbers from list
print(mo)

le=[1,10,90,70,30]
random.shuffle(le) # Randomly changes the order of a list
print(le)