def add (n1, n2):
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
    should_continue = True
    num1 = float(input("What's the first number? : "))

    while should_continue:
        for symbol in operations:
            print(symbol)
        input_operation = input("Pick an operation: +, -, *, / : ")
        num2 = float(input("What's the second number? : "))
        answer = operations[input_operation](num1, num2)
        print(f"{num1} {input_operation} {num2} = {answer}")
            
        should_continue = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation. : ")
    
        if  should_continue == "y":
            num1 = answer
        else:
            should_continue = False
            print("\n" * 10)
            calculator()

calculator()