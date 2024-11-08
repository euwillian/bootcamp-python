"""
v 1.0.1

Create a function find_highest_bidder
Adjust the variables, dict names
Adjust the While condition

"""

secret_auction_dict = {}
continue_bidding = True


def find_highest_bidder(bidding_dictionary: dict) -> None:
    name_max = ""
    max_bid = 0

    for bidder in bidding_dictionary:
        current_value_bid = bidding_dictionary[bidder]
        if current_value_bid > max_bid:
            name_max = bidder
            max_bid = current_value_bid

    print(f"The winner is {name_max} with a bid of ${max_bid}")


while continue_bidding:
    name = input("What's your name? ")
    bid = int(input("What's your bid? "))

    secret_auction_dict[name] = bid  # {name: bid}

    continue_bidding = input("Are there any other bidders? Type 'yes' or 'no'. ")

    if continue_bidding == 'no':
        continue_bidding = False
        print("\n" * 100)
        find_highest_bidder(secret_auction_dict)
    else:
        print("\n" * 100)