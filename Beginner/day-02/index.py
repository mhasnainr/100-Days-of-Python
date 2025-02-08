# Topics:

# - Data types, Numbers, Operations, Type Conversion, f-Strings

# ------------- 02: Primitive Data types

# print(len('Welcome')) # Ans. 7
# print(len(5343)) # error

# --- 1. Strings: '' or " "

# print('Welcome' [0]) # Sub-stricting: Method of pulling out a particular element
# print('Welcome' [4])

# --- 2. Ineger: Num without any decimal places

# print (423 + 434)

# --2.2: Large integers
# note: In USA and UK, etc, comma is used for large numbers
# in programming, we can use underscore [ _ ], which the system will understand it as a comma

# print(432_435_3223)

# --- 3. Float: Num with decimals

# 323.4232

# --- 4. Boolean: True or False


# ------------- 03: Quiz [Data types]: html file


# ------------- 04: Type of Error, Checking & Conversion

# num_char = len(input('Enter your name: '))
# print("Your name has " + num_char + " characters") # type error

# in order to know the data type, use 'type' function
# print(type(num_char))

# -- Type conversion: changing data type
# e.g: str(num_char). this will change integer data type to a string data type

# new_num_char = str(num_char)
# print("Your name has " + new_num_char + " characters") # correct


# --- example:

# a = 423
# print(type(a)) # <class 'int'>

# b = float(a)
# print(type(b)) # <class 'float'>

# print(4333 + float('232.32')) # 4565.32

# print(str('23') + str('4334')) # 234334


# ------------- 05: Coding Ex

# adding 2 digit numbers

# two_digit_num = input()
# print(type(two_digit_num)) # <class 'str'>

# first_digit = two_digit_num[0]
# first_digit = int(two_digit_num[0])
# second_digit = int(two_digit_num[1])

# print(first_digit + second_digit)


# ------------- 06: Operations

# 3 + 5 # add
# 3 - 2 # sub
# 6 * 2 # product

# 10/ 5 # divide: Ans. 2.0 'float' instead of 'int'

# 2**3 = 8 # exponent

# note: Concept of PEMDASLR is used when different operations are used in a single equation
# Parantheses: ()
# Exponents: **
# Multiplication: *
# Division: /
# Addition: +
# Subtraction: -
# LR: Left to right

# note: multiplication and division ar eequally prioritized
# print(3 * 3 + 3 / 3 - 3) # 7

# in order to get an answer of 3 instead of 7
# print(3 * ((3 + (3 / 3)) - 3)) # 3.0


# ------------- 07: Coding Ex: BMI Calculator

# formula: weight (kg)/ height(m square)

# height = float(input())
# weight = int(input())

# using exponent operator
# bmi = weight/ height ** 2

# or using multiplication and PEMDAS
# bmi = weight/ (height * height)

# result
# result = int(bmi)
# print(result)


# ------------- 08: Number Manipulation & f-Strings

# print(11 / 3) # 3.666_ _ _ _
# print(int(11 / 3)) # 3
# print(round(11 / 3)) # 4

# note:
# int() rounds backward
# round() rounds forward

# in order to round it to specific decimal place
# print(round(11 / 3, 2)) # 2.67

# print(round(32.4322554452, 3))  # 32.432

# print(9 // 2)  # Ans. is 4: flow division way
# print(type(9 // 2)) # 'int
# print(type(9 / 2)) # 'float'
# print(type(9 / 3)) # 'float'

# -- Number Manipulation

# score = 0

# score += 5  # 5
# score -= 2  # 3
# score *= 3  # 9
# score /= 2  # 4.5
# print(score)


# -- f-strings

# score = 0
# height = 1.5
# isWinning = True

# print(f"your score is {score}, your height is {height}, your winning news is {isWinning}")


# ------------- 09: Coding Ex: Life in Weeks

# age = int(input())
# weeks = 52
# age_in_weeks = age * 52
# avg_age = 90
# total_weeks = weeks * avg_age
# weeks_left = total_weeks - age_in_weeks

# or

# age = input()
# years = 90 - int(age)
# weeks_left = years + 52

# second method isn't giving correct answer

# print(f"Your average age left (in weeks) is {weeks_left} weeks")


# ------------- 10: Quiz [Operations]

