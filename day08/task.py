def greet():
    print("# First line")
    print("# Second line")
    print("# Third line")


greet()


# fuctions that allows for inputs

def greet_with_name(name: str) -> None:
    """
    Greet the user with their name.

    Parameters:
    name (str): The name of the user.
    """
    print(f"Hello: {name}")
    print(f"How do you do {name}?")


greet_with_name("Willian")


def life_in_weeks(age: int) -> None:
    """
    How many weeks we have left, if we live until 90 years old

    Parameters:
    age (int): The age of the user

    """

    weeks_left = 4680 - (age * 52)

    # 90 years * 52 weeks = 4680 weeks if we live until 90 years old

    print(f"You have {weeks_left} weeks left.")



