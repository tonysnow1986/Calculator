from Art import logo
def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    print(logo)
    num1 = float(input("What's the first number?: "))

    for symbol in operations:
        print(symbol)
    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation from the line above: ")
        num2 = float(input("What's the second number?: "))
        cal_function = operations[operation_symbol]
        answer = cal_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input("Type 'y' to continue calculating with the previous answer or 'n' to exit.: ") == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()

    operation_symbol = input("Pick another operation: ")
    num3 = int(input("What's the next number?: "))
    cal_function = operations[operation_symbol]
    second_answer = cal_function(cal_function(num1, num2), num3)
    print(f"{answer} {operation_symbol} {num3} = {second_answer}")

calculator()
