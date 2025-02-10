# Topics:

# Conditional Statements, Logical Operators, Code Blocks and Scope


# ------------ 03: Control flow with if else and Conditional Operators

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


# ------------ 04: Ex: Odd or Even, introducing the Modulo

# num = int(input('Enter a number: '))

# if num % 2 == 0:
#     print(f"{num} is an even number")
# else:
#     print(f"{num} is an odd number")


# ------------ 05: Nested if statements and elif statements

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


# ------------ 06: Ex: BMI 2.0

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


# ------------ 07: Ex: Leap Year

# note: Leap year has 366 days, while normal has 365 days
# Leap year comes once in four years, and in Feb

# leap year: if year % 4 == 0 and year % 100 == 0 and year % 400 == 0

year = int(input('Enter the year: '))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            # not a leap year, unless special case
            print(f"{year} is a leap year")
        else:
            print(f"{year} is not a leap year")
    else:
        print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")



# ------------ 08: Multiple if Statements in Succession

# 
