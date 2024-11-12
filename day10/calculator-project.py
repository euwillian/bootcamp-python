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


def operation(op):
    if op == "+":
        return add(first_number, second_number)
    elif op == "-":
        return sub(first_number, second_number)
    elif op == "*":
        return mul(first_number, second_number)
    elif op == "/":
        return div(first_number, second_number)
    else:
        return "Invalid Operation!"


while True:
    first_number = float(input("First number: "))
    op_choosed = input("+ - * /:  ")
    second_number = float(input("Second number: "))

    result = operation(op_choosed)

    print(f"Result: {result} continue calculating with the last result? type y/n")

    if result == "y":
        pass
    else:
        break
