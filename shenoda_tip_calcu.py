# Tip Calculator

print("Welcome to the tip calculator")
total_bill = float(input("What was the total bill? "))
tip = float(input("How much tip would you like to give? 10, 12, or 15 "))
split_bill = int(input("How many people to split the bill? "))
tip_amount = (total_bill * tip) / 100
pay = ( total_bill + tip_amount ) / split_bill
print("Each person should pay: ", pay)