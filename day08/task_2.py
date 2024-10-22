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
