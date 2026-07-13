# Conditional Statements, Logical, Blocks, Scope:
# if / els syntax
# if condition:
#     do this
# else:
#     do this

# height = round(float(input("What is the height in centimeters? "))) # if 119.5 wll consider the height = 120, because round it.
# if height >= 120:
#     print(f"your height is : ({height}) so you can ride")
# else:
#     print(f"your height is :({height}) so you can't ride")

# Modulo operator

# print ( 10 % 2)
# print ( 10 % 3)



# Even or Odd Number challenge:


# The Purpose of script to get a number from user to tell EVEN or ODD Number:

user_input = int(input("Enter a number: "))

remainder = user_input % 2

if remainder == 0:
    print(f"The number you entered is... ({user_input}) is EVEN because the remainder is {remainder} ")
else:
    print(f"The number you entered is... ({user_input}) is ODD because the remainder is {remainder} ")