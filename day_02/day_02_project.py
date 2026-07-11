# Tip Calculator
#
print("Welcome to the tip calculator")
total_bill = float(input("What was the total bill? "))
tip = float(input("How much tip would you like to give? 10, 12, or 15 "))
split_bill = int(input("How many people to split the bill? "))
tip_amount = (total_bill * tip) / 100
final_amount = ( total_bill + tip_amount ) / split_bill
print(f"Each person should pay ${final_amount:.2f}")


#Which of these lines of code will give you an error?

# name = input("What is your name?")
# print(f"Hello, {name}")
#
# name = input("What is your name?")
# print("Hello, " + name)
#
# age = 12
# print(f"You are {age} years old")

# age = 12
# print("You are " + str(age) + " years old") # this line, to correct add str(age)