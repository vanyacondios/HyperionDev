# Task 5 - Build finance calculators

import math

# Ask user to select type of calculator - investment or bond.
calculator_type = input('''investment - to calculate the amount of interest you'll earn on your investment\nbond\
       - to calculate the amount you'll have to pay on a home loan\n\nEnter \
either 'investment' or 'bond' from the menu above to proceed: ''')

# Convert user input to lower case to avoid case complications.
calculator_type = calculator_type.lower()

# Investment calculator - collect user input and print out investment value at end of period.
if calculator_type == "investment":
    deposit_amount = int(input("What is the amount of money you are depositing to the nearest pound? "))
    interest_rate = int(input("What is the interest rate? Please enter only numbers and omit the " + "%" + " sign! "))
    years = int(input("Please enter the number of years you plan on investing? "))
    interest_type = input("Do you want to calculate the return based on simple or compound interest? Please type \
\"simple\" or \"compound\" only. ")
    # Calculate interest depending whether user selects compound or simple.
    if interest_type == "simple":
        future_sum = round((deposit_amount*(1 + (interest_rate / 100)*years)),2) # this and further formulae as provided by Hyperion
        print(f"At the end of the period you will have earned £{future_sum}.")
    elif interest_type == "compound":
        future_sum = round((deposit_amount * math.pow((1 + interest_rate / 100),years)),2) # How to round a float - found on www.tutorialspoint.com
        print(f"At the end of the period you will have earned £{future_sum}.")
    else:
        print("Please check spelling and enter either simple or compound. ") # At this point program will stop and need to be restarted.

# Bond calculator - collect user input and print out amount of monthly repayment.
elif calculator_type == "bond":
    house_value = int(input("What is your property currently worth? "))
    bond_interest = int(input("What is the loan interest rate? "))
    months_length = int(input("Over how many months will you repay the bond? "))
    repayment = round((bond_interest/100/12 * house_value)/(1 -(1 + bond_interest/100/12)**(-months_length)), 2)
    print(f"Your monthly repayment will be £{repayment}.")
else:
    print("Please check spelling and enter either bond or investment.") # At this point program will stop and need to be restarted.