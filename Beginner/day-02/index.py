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

