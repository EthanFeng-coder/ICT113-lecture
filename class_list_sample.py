import random

myList = [1, 2, 3, 4, 5]

# Pick a single random item
print(random.choice(myList))

# Pick 3 random unique items
print(random.sample(myList, 3))

# Shuffle the list in place
random.shuffle(myList)
print(myList)