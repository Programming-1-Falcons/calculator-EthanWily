while True:
    operation = input("Please enter an operation: ")
    num1 = float(input("Please enter a number: "))
    num2 = float(input("Please enter another number: "))
    if operation == "+":
        solution = num1 + num2
        print(num1, "+", num2, "=", solution)
    elif operation == "-":
        solution = num1 - num2
        print(num1, "-", num2, "=", solution)
    elif operation == "/":
        solution = num1 / num2
        print(num1, "/", num2, "=", solution)
    elif operation == "*":
        solution = num1 * num2
        print(num1, "*", num2, "=", solution)
    elif operation == "**":
        solution = num1 ** num2
        print(num1, "**", num2, "=", solution)
    else:
        print("Sorry, that didn't work! Please try again.")
