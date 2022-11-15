print("Calculator")
operation = input("What operation? ") # This is asking for the operation to calculate on.
if operation == "+":
    num_1 = int(input("Number 1: "))
    num_2 = int(input("Number 2: "))
    ans = num_1 + num_2                  # This Calculates The Answer.
    print(f"{num_1} + {num_2} = {ans}")
if operation == "-":
    num_1 = int(input("Number 1: "))
    num_2 = int(input("Number 2: "))
    ans = num_1 - num_2                  # This Calculates The Answer.
    print(f"{num_1} - {num_2} = {ans}")
if operation == "/":
    num_1 = int(input("Number 1: "))
    num_2 = int(input("Number 2: "))
    ans = num_1 / num_2                  # This Calculates The Answer.
    print(f"{num_1} / {num_2} = {ans}")
if operation == "*":
    num_1 = int(input("Number 1: "))
    num_2 = int(input("Number 2: "))
    ans = num_1 * num_2                  # This Calculates The Answer.
    print(f"{num_1} x {num_2} = {ans}")