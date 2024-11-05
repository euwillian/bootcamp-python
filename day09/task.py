programming_dictionary = {"apple": "red", "pear": "green", "banana": "yellow", "starwberry": "red"}

# add new item

print(programming_dictionary)

# empty dict

empty_dict = {}

# add items
empty_dict["item1"] = "new item"
# edit an item in a dictionary
empty_dict["item1"] = "edit item"
print(empty_dict)

# loop in a dictionary

for items in programming_dictionary:
    print(f"{items}: {programming_dictionary[items]}")

