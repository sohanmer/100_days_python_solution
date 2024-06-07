import random

names = ['Angela', 'Ben', 'Jenny', 'Michael', 'Chloe']

print(f'{random.choice(names)} is going to buy the meal today!')



## Another way ##
# num_items = len(names)
# # Generate random numbers between 0 and the last index. 
# random_choice = random.randint(0, num_items - 1)
# # Choose and print a random name.
# print(names[random_choice])
