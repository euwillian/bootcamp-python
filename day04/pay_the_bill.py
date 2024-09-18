# Challenge Who will pay the bill?
import random

friends = ["Alice",
           "Bob",
           "Charlie",
           "David",
           "Emmanuel"]

# random_name = friends[random.randint(0, 5)] # Other way 1
# random_name = friends[random.randint(0, len(friends) - 1)] # Other way 2

random_name = random.choice(friends) 

print(f"{random_name} will pay the bill")