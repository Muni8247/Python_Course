'''1️⃣ Generate a random number between 50 and 100.
2️⃣ Pick a random name from ["Alice", "Bob", "Charlie", "David"].
3️⃣ Shuffle the list [10, 20, 30, 40, 50] and print the new order.
4️⃣ Generate 5 unique random numbers between 1 and 20.
5️⃣ Simulate a dice roll (random number between 1 and 6).'''

#(1)

import random

ab=random.randint(50,100)
print(ab)
# (2)

bc=["Alice", "Bob", "Charlie", "David"]
print(random.choice(bc))

#(3)
li=[10, 20, 30, 40, 50]
random.shuffle(li)
print(li)

# (4)
cd=random.sample(range(1,20), 5)
print(cd)

# (5)
roll=random.randint(1,6)
print(f"you rolled a: {roll}")