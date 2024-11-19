import blackjack_art
import random

"""
Our BlackJack Game Rules:

- the deck is unlimited in size
- there are no jokes
- the Jack/Queen/King all count as 10
- The Ace can count as 11 or 1
- Use the following list as the deck of cards:

cards = [11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

- The cards in the lista have equal probabily of being drawn
- Cards are not removed from the deck as they are drawn
- The computer is the Dealer


"""


def user_total(user_list: list) -> int:
    """
    return the total sum of user list

    """
    user_list_total = 0

    for i in user_list:
        user_list_total += i

    return user_list_total


def dealer_total(dealer_list: list) -> int:
    """
    return the total sum of dealer list

    """
    dealer_list_total = 0

    for i in dealer_list:
        dealer_list_total += i

    return dealer_list_total


cards = [11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# var1 = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

user_list_cards = [random.choice(cards), random.choice(cards)]
dealer_list_cards = [random.choice(cards)]
print(user_list_cards)
print(dealer_list_cards)
print(user_total(user_list_cards))
print(dealer_total(dealer_list_cards))




"""
Your cards: [10,4], current score: 14
    Computer's first card: 5
Type 'y' to get another card, type 'n' to pass: n


--

Your final hand: [10,4,5], final score: 19
   Computer's final hand: [5,6,1,3,10], final score: 25
Opponent went over. You win 😁
Do you want to play a game of Blackjack? Type 'y' or 'n':


"""
