# add
def add(n1, n2) -> float:
    return n1 + n2


# subtract
def sub(n1, n2) -> float:
    return n1 - n2


# divide
def div(n1, n2) -> float:
    return n1 / n2


# Multiply
def mul(n1, n2) -> float:
    return n1 * n2


first_number = float(input("First number: "))

while True:

    operations = {
        "+": add,
        "-": sub,
        "*": mul,
        "/": div
    }

    operation_symbol = input("+ - * /:  ")
    second_number = float(input("Second number: "))

    result = operations[operation_symbol](first_number, second_number)  # operations[]()

    print(f"{first_number} {operation_symbol} {second_number} = {result}")
    continue_calc = input(f"Result: {result} continue calculating with the last result? type y/n: ")

    if continue_calc == "y":
        first_number = result
    else:
        break
