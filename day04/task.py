# random Module
import random
import my_module

# random_integer = random.randint(1, 10)
# print(random_integer)

# print(my_module.my_favourite_number)


# Game - Heads or Tails

cont = 0
count_head = 0
count_tail = 0

while cont != 50:
    
    random_coin = random.randint(0, 1)
    
    if random_coin == 0:
        print("Head")
        count_head += 1
    else:
        print("Tail")
        count_tail += 1
    cont += 1

print(f"Head {count_head}")
print(f"Tail {count_tail}")
