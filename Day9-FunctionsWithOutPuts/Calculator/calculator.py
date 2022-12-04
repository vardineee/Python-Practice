from art import logo

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return(num1 * num2)

def divide(num1,num2):
    return num1 /num2

operations = {
    "+": add,
    "-": subtract,
    '*': multiply,
    "/": divide
}

def calculate():
    print(logo)
    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)

    should_continue =True
    while should_continue:
        chosen_symbol = input("Pick an operation from the live above: ")
        num2 = float(input("What's the next number?: "))
        for key, value in operations.items():
            if key == chosen_symbol:
                result = value(num1,num2)

        print(f"{num1} {chosen_symbol} {num2} = {result}")

        should_continue = True
        calculate_again = input(f"Type 'y' to continue calculating with {result} or type 'n' to start again: ").lower()
        if calculate_again == 'y':
            num1 = result
        else:
            should_continue = False
            calculate()
calculate()
