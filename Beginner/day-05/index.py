# Topics:

# For loops, Range & Code Blocks

# ---------------------------- 02: Using for loop with Python list

# fruits = ['Apple', 'Mango', 'Grapes']
# for fruit in fruits:
#     print(fruit)  # Ans: Apple, Mango, Grapes
# print(fruits) # Ans:  ['Apple', 'Mango', 'Grapes'], 3 times print b/c of 3 items in the list

# BTS: each time a fruit's value is assigned a variable named 'fruit'

# print(fruit + 'Pie')  # Apple, ApplePie, Mango, MangoPie, Grapes, GrapesPie

# print(fruits)  # Ans:  ['Apple', 'Mango', 'Grapes'], only once

#

# ---------------------------- 03: Ex: Average Height

# student_heights = input().split()
# for n in range(0, len(student_heights)):
#     student_heights[n] = int(student_heights[n])

# total_height = 0
# for height in student_heights:
#     total_height += height
# print(f"total height = {total_height}")

# num_of_students = 0
# for student in student_heights:
#     num_of_students += 1
# print(f"Number of students = {num_of_students}")

# avg_height = round(total_height / num_of_students)
# print(f"Average height = {avg_height}")

#

# ---------------------------- 04: Ex: High Score

# scores = input().split()
# for n in range(0, len(scores)):
#     scores[n] = int(scores[n])

# highest_score = 0
# for score in scores:
#     if score > highest_score:
#         highest_score = score
#         print(highest_score)

# print(f"The highest score in the class is: {highest_score}")

#

# ---------------------------- 05: for loop & Range()

# ---- for loop with range
# range(start, one-step before ending, diff b/w two numbers)


# for num in range(1, 11, 3):
#     print(num)  # 10 is excluded, so write 11 to include 10


# task: add numbers b/w [inclusive] 1 and 100

# total = 0
# for num in range(1, 101):
#     total += num
# print(total)

#

# ---------------------------- 06: Ex: Adding even numbers

# target = int(input())  # num b/w 0 and 1000
#
# even_sum = 0

# 1st method

# for num in range(2, target + 1, 2):
#     even_sum += num
# print(even_sum)

# 2nd method

# for num in range(1, target + 1):
#     if num % 2 == 0:
#         even_sum += num
# print(even_sum)

#

# ---------------------------- 07: Ex: FizzBuzz

# target = 100
# for num in range(1, target + 1):
#     if num % 3 == 0 and num % 5 == 0:
#         print('FizzBuzz')
#     elif num % 3 == 0:
#         print('Fizz')
#     elif num % 5 == 0:
#         print('Buzz')
#     else:
#         print(num)
