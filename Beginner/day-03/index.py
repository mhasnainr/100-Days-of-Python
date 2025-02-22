# Topics:

# Conditional Statements, Logical Operators, Code Blocks and Scope


# ---------------------- 03: Control flow with if else and Conditional Operators

# print("Welcome to the Rollercoaster Ride!")
# height = int(input("Enter your height (in cm): "))

# if height >= 120: # writing: height = 120 , will show an error
#     print('You are eligible to ride')
# else:
#     print('You are not eligible to have the ride')


# following are Comparison Operators:
# >, <, >=, <=, ==, !=

# single equals to [=]: means you are assigning the value with the varialbe
# double equals [==]: means checking equality, whether the value at left matches with te value at right or not


# ---------------------- 04: Ex: Odd or Even, introducing the Modulo

# num = int(input('Enter a number: '))

# if num % 2 == 0:
#     print(f"{num} is an even number")
# else:
#     print(f"{num} is an odd number")


# ---------------------- 05: Nested if statements and elif statements

# height = int(input("Enter your height (in cm): "))

# if height >= 120:
#     print('You are eligible to ride')
#     age = int(input('Enter your age: '))
#     if age < 12:
#         print('Please pay $5')
#     elif age <=18:
#         print('Please pay $7')
#     else:
#         print('Please pay $12')
# else:
#     print('You are not eligible to have the ride')


# ---------------------- 06: Ex: BMI 2.0

# formula: weight / height squared

# weight = int(input('Enter your weight [in kg]: '))
# height = float(input('Enter your height [in m]: '))

# bmi = weight / (height * height)
# if bmi < 18.5:
#     print(f"Your BMI is {bmi:.2f}, so you are under-weight")
# elif bmi < 25:
#     print(f"Your BMI is {bmi:.2f}, so you have a normal weight")
# elif bmi < 30:
#     print(f"Your BMI is {bmi:.2f}, so you are slightly weight")
# elif bmi < 35:
#     print(f"Your BMI is {bmi:.2f}, so you are obese")
# else:
#     print(f"Your BMI is {bmi:.2f}, so you are clinically obese")


# ---------------------- 07: Ex: Leap Year

# note: Leap year has 366 days, while normal has 365 days
# Leap year comes once in four years, and in Feb

# leap year: if year % 4 == 0 and year % 100 == 0 and year % 400 == 0

# year = int(input('Enter the year: '))

# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             # not a leap year, unless special case
#             print(f"{year} is a leap year")
#         else:
#             print(f"{year} is not a leap year")
#     else:
#         print(f"{year} is a leap year")
# else:
#     print(f"{year} is not a leap year")


# ---------------------- 08: Multiple if Statements in Succession

# height = int(input("Enter your height (in cm): "))
# bill = 0

# if height >= 120:
#     print('You are eligible to ride')
#     age = int(input('Enter your age: '))
#     if age < 12:
#         bill = 5
#         print('Child tickets are: $5')
#     elif age <= 18:
#         bill = 7
#         print('Youth tickets are: $7')
#     else:
#         bill = 12
#         print('Adult tickets are: $12')

#     wants_photo = input('Do you want a photo taken? Y or N. ').upper()
#     if wants_photo == 'Y':
#         # Add $3 to the bill
#         bill += 3
#         print(f"Your final bill is ${bill}")
#     elif wants_photo == 'N':
#         print(f"Your final bill is ${bill}")
#     else:
#         print('Press Y or N')
# else:
#     print('You are not eligible to have the ride')


# ---------------------- 09: Ex: Pizza Order

# print('Thank you for choosing Python Pizza Deliveries')
# bill = 0

# size = input('What size piece do you want? S, M, L. ').upper()
# if size == 'S':
#     bill += 15
# elif size == 'M':
#     bill += 20
# elif size == 'L':
#     bill += 25

# add_pepperoni = input('Do you want Pepperoni? Y or N. ').upper()
# if add_pepperoni == 'Y':
#     if size == 'S':
#         bill += 2
#     elif size == 'M':
#         bill += 3
#     elif size == 'L':
#         bill += 3
# else:
#     print('Ok.')

# extra_cheese = input('Do you want extra cheese? Y or N. ').upper()
# if extra_cheese == 'Y':
#     bill += 1
# else:
#     print('Ok.')

# print(f"Your final bill is: ${bill}")


# ---------------------- 10: Logical Operators [and, or, not]

# height = int(input("Enter your height (in cm): "))
# bill = 0

# if height >= 120:
#     print('You are eligible to ride')
#     age = int(input('Enter your age: '))
#     if age < 12:
#         bill = 5
#         print(f"Child tickets are: ${bill}")
#     elif age <= 18:
#         bill = 7
#         print(f"Youth tickets are: ${bill}")
#     elif age >= 45 and age <= 55:
#         print('Everything is going to be ok. Have a free ride!')
#     else:
#         bill = 12
#         print(f"Adult tickets are: ${bill}")

# else:
#     print('You are not eligible to have the ride')


# ---------------------- 11: Ex: Love Calculator

# print('The Love Calculator is calculting your score ...')
# name1 = input('Enter your name: ')
# name2 = input('Enter your name: ')
# combined_names = name1 + name2
# lower_names = combined_names.lower()

# t = lower_names.count('t')
# r = lower_names.count('r')
# u = lower_names.count('u')
# e = lower_names.count('e')
# first_digit = t + r + u + e

# l = lower_names.count('l')
# o = lower_names.count('o')
# v = lower_names.count('v')
# e = lower_names.count('e')
# second_digit = l + o + v + e

# score = int(str(first_digit) + str(second_digit))
# if (score < 10) or (score > 90):
#     print(f"Your score is: {score}, you go together like ...")
# elif (score >= 40) and (score <= 50):
#     print(f"Your score is: {score}, you are alright together")
# else:
#     print(f"Your score is: {score}")


# note: print(''' ''') is used for multi-line strings

# print('You\re at a crossroad, where do you want to go? Type "left". ')
