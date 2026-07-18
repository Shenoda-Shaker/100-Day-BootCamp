# ATM machine mini project Ver 1.0
ACCOUNT_PIN = 1234
ACCOUNT_BALANCE = 3500

print ("#------- Marlie Bank -------# ")

pin_code = int(input("Please enter your PIN CODE to continue: "))
if pin_code == ACCOUNT_PIN:
    print ("Welcome to Marlie Bank \n")
else:
    print("\n #------- Thanks for choosing Marlie Bank -------# ")
    exit()

user_choice = input("Please choose the operation #Number : \n 1-Check Balance. \n 2-Deposit. \n 3-Withdraw. \n")
if user_choice == "1":
    print(f"Your balance is ${ACCOUNT_BALANCE:.2f} \n")
    print("#------- Thanks for choosing Marlie Bank -------# ")

elif user_choice == "2":
    deposit_amount = float (input("How much would you like to deposit? "))
    if deposit_amount <= 0:
        print("Invalid amount \n")
        print("#------- Thanks for choosing Marlie Bank -------# ")

    else:
        ACCOUNT_BALANCE += deposit_amount
        print(f"Your new balance is ${ACCOUNT_BALANCE:.2f} \n")
        print("#------- Thanks for choosing Marlie Bank -------# ")


elif user_choice =="3":
    withdraw_amount = float (input("How much would you like to withdraw? "))
    if withdraw_amount <= 0:
        print("\n Invalid amount")
    elif withdraw_amount > ACCOUNT_BALANCE:
        print("\n Insufficient balance")
        print("\n #------- Thanks for choosing Marlie Bank -------#")

    else:
        ACCOUNT_BALANCE -= withdraw_amount
        print(f"\n Your new balance is ${ACCOUNT_BALANCE:.2f} \n")
        print("#------- Thanks for choosing Marlie Bank -------# ")


else:
    print("Invalid choice \n")
    print("#------- Thanks for choosing Marlie Bank -------# ")
