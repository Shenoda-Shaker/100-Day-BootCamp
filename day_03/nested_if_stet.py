# Nested if statements & elif statement

# RollerCoaster game check:

player_height = int(input("Please enter your height in CM: "))
if player_height >= 120:
    print("You can play")
    player_age = int(input("Please enter your age in years: "))
    if player_age >= 18:
        print("Pay $12")
    elif 12 <= player_age < 18:
        print("Pay $7")
    else:
        print("Pay $5")

else:
    print("Sorry! you can't play")