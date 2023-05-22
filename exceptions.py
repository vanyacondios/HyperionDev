# Task 9 - Ask user if they want to perform calculation or display equations. Collect equations input. Perform calculations, write to file, display content.
# Resubmission - new lines 24, 25, 32, 33. Not sure we have been taught to define functions for operations or what is meant exactly.

user_selection = input("Would you like to perform a calculation (1) or see existing calculations (2)? Please enter 1 or 2: ")
while user_selection != "1" and user_selection != "2":
    user_selection = input("Invalid input. Please enter 1 to perform a calculation or 2 to display existing calculations: ")

if user_selection == "1":
    print("\nThis program will perform a calculation based on two numbers and an operator and will write the result to a file.")
    #  Start off with loop to ensure calculator allows user to enter more than one equation until user decides to stop.
    while True:
        # Collect input, making sure user is asked repeatedly if input is of wrong type.
        with open('equations.txt',  'a+') as file:   # a+ parameter creates a file if one does not exist and writes to it in append mode, so that previous equations are not deleted
            while True:
                try:
                    num1 = float(input("\nPlease enter a number: "))
                    break
                except Exception:
                    print("This was not a valid number. Please try again: ")
            while True:
                try:
                    num2 = float(input("\nPlease enter a second number: "))
                    if num2 == 0:
                        num2 = float(input("You cannot divide by 0. Please enter a different number or reenter 0: "))
                    break
                except Exception:
                    print("This was not a valid number. Please try again: ")
            operator = input("\nPlease enter an operator. You can enter +, -, *, / or %: ")
            while operator != "+" and operator != "-" and operator != "*" and operator != "/" and operator != "%":
                operator = input("This was not a valid operator. Please enter +, -, *, / or %: ")
            while operator == "/" and num2 == 0:
                operator = input("You cannot divide by 0. Please enter a different operator: ")
            # Calculate result and write to file
            if operator == "+":
                result = num1 + num2
            elif operator == "-":
                result = num1 - num2
            elif operator == "*":
                result = num1 * num2
            elif operator == "/":
                result = num1 / num2
            elif operator == "%":
                result = num1 % num2
            result = round(result, 2)
            file.write(f"{num1} {operator} {num2} = {result}\n")  
            print(f"\nBased on the numbers and operator entered the result is {result}.\n")
        # Ask user if they wish to exit or continue with next calculation
        userexit = input("To exit type y. To continue with the next calculation, enter anything else. ")
        if userexit == "y":
            break
# If initial input is 2 - display equations - making sure user enters the name of an existing file (equations.txt)     
else:
    while True:
        try:
            file_name = input("\nPlease enter the file name: ")
            with open(file_name,  'r') as file: 
                print(file.read())
            break
        except FileNotFoundError:
            print("Invalid file name. Please try again. ")