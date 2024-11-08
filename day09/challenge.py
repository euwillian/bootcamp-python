"""
v 1.0.0


"""

secret_auction = {}
more_bidders = True
max_bid = 0
name_max = ""

while more_bidders:
    name = input("What's your name? ")
    bid = int(input("What's your bid? "))

    secret_auction[name] = bid  # {name: bid}

    more_bidders = input("Are there any other bidders? Type 'yes' or 'no'. ")

    if more_bidders != 'yes':
        more_bidders = False
        print("\n" * 100)


for items in secret_auction:
    current_value_bid = secret_auction[items]
    if current_value_bid > max_bid:
        name_max = items
        max_bid = current_value_bid

print(f"The winner is {name_max} with a bid of ${max_bid}")
