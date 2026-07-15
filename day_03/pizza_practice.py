# Pizza Practice
# What size of pizza do you want  ( S = 15$, M = 20$, L = 25$ )
# Do you want Pepperoni on your pizza = Small +2$ # Pepperoni for Medium or Large pizza = +3$
# Do you want extra cheese = +1$

print ("Welcome to Marlie Pizza Shop")

LARGE_PIZZA_PRICE = 25
MEDIUM_PIZZA_PRICE = 20
SMALL_PIZZA_PRICE = 15

PEPPERONI_ADD_SMALL = 2
PEPPERONI_ADD_MEDIUM_LARGE = 3

EXTRA_CHEESE = 1
price = 0

pizza_user_choice = input("What the size of pizza would you like? s for SMALL / m for MEDIUM / l for LARGE: ")
if pizza_user_choice == "l":
    price += LARGE_PIZZA_PRICE
elif pizza_user_choice == "m":
    price += MEDIUM_PIZZA_PRICE
elif pizza_user_choice == "s":
    price += SMALL_PIZZA_PRICE
else:
    print("Invalid choice, please try again")

pepperoni_add = input("Would you like pepperoni? y for yes or n for no: ")
if pepperoni_add == "y":
    if pizza_user_choice == ("l", "m") :
       price += PEPPERONI_ADD_MEDIUM_LARGE
    elif pizza_user_choice == "s":
       price += PEPPERONI_ADD_SMALL

extra_cheese = input("Would you like extra cheese? y for yes or n for no: ")
if extra_cheese == "y":
    price += EXTRA_CHEESE

print(f"Your total bill is $ {price}")