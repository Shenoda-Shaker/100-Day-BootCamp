# for remember
print (" Welcome to the tip calculator")
bill = float(input("What was the total bill? " ))
tip = float(input("how much tip would you like to give? 10,12 or 15? " ))
split_bill = int(input("How many people to split the bill? "))
net_bill = (bill * tip ) / 100
total_bill = (bill + net_bill ) / split_bill
print(f"Each person should pay {total_bill:.2f} USD" )