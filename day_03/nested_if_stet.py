# Nested if statements & elif statement

# ------------------------------- RollerCoaster game check + price: -------------------------------

# player_height = int(input("Please enter your height in CM: "))
# if player_height >= 120:
#     print("You can play")
#     player_age = int(input("Please enter your age in years: "))
#     if player_age >= 18:
#         print("Pay $12")
#     elif 12 <= player_age < 18:
#         print("Pay $7")
#     else:
#         print("Pay $5")
#
# else:
#     print("Sorry! you can't play")


# ------------------------------- RollerCoaster game check + price + photo: -------------------------------

# adult = 12
# teenager = 7
# child = 5
# photo = 3
#
# player_height = int(input("Please enter your height in CM: "))
# if player_height >= 120:
#     print("Yes! you can play")          #Close else
#
#     player_age = int(input("Please enter your age in years: "))
#     if player_age >=18:
#         take_photo = input("Do you want to take a photo? (y/n): ")
#         if take_photo =="y":
#             print(f"your total ticket is $ {adult+photo}")
#         else:
#             print(f"You pay $ {adult}")
#     elif 12 <= player_age < 18:
#         take_photo = input("Do you want to take a photo? (y/n): ")
#         if take_photo == "y":
#             print(f"your total ticket is $ {teenager + photo}")
#         else:
#             print(f"You pay $ {teenager}")
#     else:
#             take_photo = input("Do you want to take a photo? (y/n): ")
#             if take_photo == "y":
#                 print(f"your total ticket is $ {child + photo}")
#             else:
#                 print(f"You pay $ {child}")
#
# else:
#     print("Sorry! you can't play")


# ------------------------------- RollerCoaster game check + price + photo ( DRY ): -------------------------------

# adult = 12
# teen_age = 7
# child = 5
# photo = 3
#
# player_height = int(input("Please enter your height in CM: "))
# if player_height >= 120:
#     print ("Yes! you can play")
#
#     player_age = int(input("Please enter your age: "))
#     if player_age >=18:
#         ticket_price = adult
#     elif 12 <= player_age < 18:
#         ticket_price = teen_age
#     else:
#         ticket_price = child
#
#     take_photo = input("would you like to take a photo? y/n: ")
#     if take_photo == "y":
#         ticket_price += photo
#     print(f"your total price is ${ticket_price}")
#
#
# else:
#     print("Sorry! you can't play")
#
# # ------------------------------- RollerCoaster game check + price + photo ( Another solution ): -------------------------------
#
# player_height = int(input("Please enter your height in centimeters: "))
# if player_height >=120:
#     print("Yes! you can play the game.")
#
#     player_age = int(input("Please enter your age in years: "))
#     if player_age >= 18:
#         bill = 12
#     elif 12 <= player_age < 18:
#         bill = 7
#     else:
#         bill = 5
#     take_photo = input("Do you would like to take a photo? y for Yes / n or NO: ")
#     if take_photo == "y":
#         bill += 3
#     print(f"the total bill is $ {bill}" )
# else:
#     print("Sorry! you can't play")