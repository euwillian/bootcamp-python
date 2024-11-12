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


operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div
}

while True:

    first_number = float(input("First number: "))
    op_choosed = input("+ - * /:  ")
    second_number = float(input("Second number: "))

    result = operations[op_choosed](first_number, second_number)  # operations[]()

    continue_calc = input(f"Result: {result} continue calculating with the last result? type y/n")

    if continue_calc == "y":
        pass
    else:
        break
