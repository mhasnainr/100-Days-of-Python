# Topics:

# Randomisation & Python List


# Link: https://askpython.com/
# search for 'random modules', etc

# ------------------------ 02: Random Module

# note: write 'import' for using random numbers in Python

import random

# random_integer = random.randint(1, 15)
# print(random_integer)

# each time it will random whole numbers, inclusive of the range provided


# ---------- Module: In order to spilt multiple functionalities of a complex project in different parts, modules are made for making the collaborative, efficient, etc


# --- follow steps to make custom modules

# 1. make a new file
# 2. for e.g; write: pi = 3.14159246
# 3. in main '.py' file, write:

# 4. import my_module
# 5. print(my_module.pi) # Ans: 3.14159246


# ---- random floating point numbers: generates any number b/w 0 and 1

# random_float = random.random()
# print(random_float)


# --- task: create a random decimal number b/w 0 and 5
# note: since float takes values b/w: 0.00000 - 0.999999...

# multiply the variable with the number

# randomFloat = random.random() * 5
# print(randomFloat)

# updated results: 0.0000... - 4.999999... [exclusive of 5]

# love_score = random.randint(1, 100)
# print(f"Your love score is {love_score}")


# ------------------------ 03: Ex: Heads or Tails

# toss = random.randint(0, 1)
# print(toss)
# if toss == 0:
#     print('Tails')
# else:
#     print('Heads')


# ------------------------ 04: Understanding the Offset and Appending Items to Lists

# List: It's a data structure, way of organising and storing data in Python
# although variables were used for storing of data [but for individual only]

# e.g; in order to store names of multiple states of a country, the concept of 'list' is introduced

# at times, order is also important, so lists are used
# writing way [for e.g;]: fruits = [item1, item2]

# states_of_america = ["Delaware", "Pennsylvania"]

# print(states_of_america[0]) # ascending
# print(states_of_america[-1]) # descending


# in programming:
# ascending order starts from 0
# descending order starts from -1, the end

# --- in order to change the list[item]

# states_of_america[1] = 'Pencilvania'
# print(states_of_america)


# --- append(): adding an item at the end of the list

# states_of_america.append('California')
# print(states_of_america)


# ---- extend(): add another list inside a list
# states_of_america.extend(['New Mexico', 'Texas'])
# print(states_of_america)


# ------------------------ 05: Ex: Who'll pay the bill


# friends_string = input("Enter names separated by a comma: ")
# names: ali, asif, bilal, kashif

# Split the input string into a list of names.
# friends = friends_string.split(", ")

# Get the total number of items in the list.
# num_items = len(friends)

# Generate a random index between 0 and num_items - 1.
# random_choice = random.randint(0, num_items - 1)

# Select the friend at the randomly generated index.
# bill_payer = friends[random_choice]

# print(f"{bill_payer} is going to pay the bill today!")


# ------------------------ 06: IndexErrors and working with Nested Lists

# states_of_america = ["Delaware", "Pennsylvania", 'New Mexico', 'Texas']
# print(len(states_of_america))  # 4

# print(states_of_america[4])  # IndexError: list index out of range

# or

# num_of_states = len(states_of_america)
# print(states_of_america[num_of_states])  # IndexError: list index out of range

# ---- solution for Index error
# writing ' -1 ' will covert 1 to 0, 4 becomes 3, etc
# print(states_of_america[num_of_states - 1])

# ----- Nested lists

# example
# dirty_dozen = ['Peach', 'Pineapple', 'Watermelon', 'Spinach', 'cabbage',
#                'Apple', 'Papaya', 'Banana', 'coriander', 'basil', 'Mango', 'Grapes']

# vegetables = ['Spinach', 'cabbage', 'coriander', 'basil']

# fruits = ['Apple', 'Papaya', 'Banana', 'Peach',
#           'Pineapple', 'Watermelon', 'Mango', 'Grapes']

# dirty_dozen = [vegetables, fruits]

# print(dirty_dozen)  # brackets inside bracket will show up b/c of multiple lists


# --- example

# fruits = ["Strawberries", "Nectarines", "Apples",
#           "Grapes", "Peaches", "Cherries", "Pears"]
# vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

# dirty_dozen = [fruits, vegetables]
# print(dirty_dozen[1][2])  # Vegetables [1] --> Tomatoes [2]


# --- example

# fruits = ["Strawberries", "Nectarines", "Apples",
#           "Grapes", "Peaches", "Cherries", "Pears"]

# fruits[-1] = "Melons" # this replaces Pears with Melons


# fruits.append("Lemons")
# print(fruits)

# Ans: ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Melons", "Lemons"]


# ------------------------ 07: Quiz [ List and IndexError ]


# ------------------------ 08: Ex: Treasure Map

# 🪎 🏴‍☠️

# line1 = ['🏴', '🏴', '🏴']
# line2 = ['🏴', '🏴', '🏴']
# line3 = ['🏴', '🏴', '🏴']

# map = [line1, line2, line3]
# print("Hiding your treasure: X marks the spot.")
# position = input()
#

# letter = position[0].lower()
# abc = ['a', 'b', 'c']
# letter_index = abc.index(letter)
# num_index = int(position[1]) - 1
# map[num_index][letter_index] = 'X'
#

# print(f"\n{line1}\n{line2}\n{line3}")


# ------------------------ 09: Project: Rock, Paper and Scissors

#
