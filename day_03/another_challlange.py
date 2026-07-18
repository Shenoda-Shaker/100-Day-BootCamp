# Cinema Ticketing System Ny Marlie Co.

ADULT_TICKET_PRICE = 18
TEEN_TICKET_PRICE = 13
CHILD_TICKET_PRICE = 5

GLASSES_3D = 2

POPCORN = 4

total_bill = 0

client_age = int(input("What is your age? "))
if client_age < 5:
    print("Sorry! you are too young to enter cinema!")
    exit(0)
elif 5 >= client_age <= 12:
    total_bill = CHILD_TICKET_PRICE
elif 13 <= client_age <= 17:
    total_bill = TEEN_TICKET_PRICE
elif client_age >= 18:
    total_bill = ADULT_TICKET_PRICE
print("Welome")

glasses_3d = input("Would you like a 3D glasses? (y/n) ")
if glasses_3d == "y":
    total_bill += GLASSES_3D


pop_corn = input("Would you like a pop corn? (y/n) ")
if pop_corn == "y":
    total_bill +=POPCORN
else:
    total_bill = total_bill

print(f"Your total bill is$ {total_bill}, Welcome to our cinema")