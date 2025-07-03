# Import the math module
import math

# Introductory Message
print("_-_-_-_Welcome to The Financial Calculator_-_-_-_")


# Applied a while loop to improve user experience 
# for inavlid inputs
while True:
    # Request the user to enter investment or bond 
    # and remove case sensitivity using .lower()
    # to lowercase the user input
    choice = input('''
    Please enter a either Bond or Investment:

    💲Investment - to calculate the amount of interest you'll earn on 
    your investment. 
               
    💰 Bond - to calculate the amount you'll have to pay on a home 
    loan.

    Selection: ''').strip().lower()
    print("Thank you for your selection!!")

    # Based on user input, use conditional statements to
    # handle accordingly
    # If the user inputs investment
    if choice == "investment":
        # Casting to float to account for cents and decimals
        investment_amount = float(input("Please enter the amount you would like to invest: "))
        interest_rate = float(input("Please enter the interest rate as a value only: e.g 10: "))
        investment_period = float(input("Enter the number of years you would like to invest: "))
        interest_type = input("Please choose the interest type Simple or Compound: ").lower()
        
        # Use nested conditional statement for interest type
        # Simple interest calculation
        if interest_type == "simple":
            simple_amount = investment_amount * (1 + (interest_rate / 100) * investment_period)  # Simple interest equation
            round_simple = round(simple_amount, 2)  # Rounding off to cents as we are working with currency
            print(f"Your simple interest investment for the peiod of {investment_period} years is R{round_simple}")
            break
            
    # Compund interest calculation
        elif interest_type == "compound":
            compound_amount = investment_amount * (1 + (interest_rate / 100))**investment_period  # Compound interest equation
            round_compound = round(compound_amount, 2)  # Rounding off to cents as we are working with currency
            print(f"Your compound interest investment for the period of {investment_period} years is R{round_compound}.")
            break

            # Handle invalid inputs
        else:
            print("❌ You have entered an invalid selection. Going back to main menu")
        
        # If the user input bond
    elif choice == "bond":
        present_house_value = float(input("Please enter the present value of the house: "))
        interest_rate = float(input("Please enter the interest rate: "))
        final_interest = (interest_rate / 100) / 12
        repayment_period = float(input("Please enter the number of months you would like to repay: "))
        repayment_amount = (final_interest * present_house_value) / (1 - (1 + final_interest) ** (-repayment_period))  # Bond equation
        round_repayment = round(repayment_amount, 2)  # Rounding off to cents as we are working with currency
        print(f"Your repayment is R{round_repayment} per month over {repayment_period} months.")
        break

        # Invalid inputs 
    else:
        print("❌ You have entered an invalid selection. Please try again.")

        
        