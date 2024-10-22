# fuctions with more than 1 input

def greet_with(name: str, location: str) -> None:
    """
    Greet the user with their name and location.

    Parameters:
    name (str): The name of the user.
    location (str): The location of the user.
    """
    print(f"Hello {name}")
    print(f"What's it like in {location}")


greet_with("Willian", "São Paulo")

# Keyword Arguments
greet_with(name="Willian", location="São Paulo")


def calculate_love_score(name1: str, name2: str) -> str:
    """
    1. Take both people's names and check for the number of times the letters in the word TRUE occurs.

    2. Then check for the number of times the letters in the word LOVE occurs.

    3. Then combine these numbers to make a 2-digit number and print it out.

    """

    is_true = "true"
    is_love = "love"

    combined_name = (name1 + name2).lower()
    cont_true = 0
    cont_love = 0

    for i in range(4):
        cont_true += combined_name.count(is_true[i])
        cont_love += combined_name.count(is_love[i])

    return str(cont_true) + str(cont_love)


print(calculate_love_score("Angela Yu", "Jack Bauer"))
print(calculate_love_score("Willian Santos", "Giovana Lopes"))
