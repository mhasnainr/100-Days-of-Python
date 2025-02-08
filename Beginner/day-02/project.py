# ------------- 11: Tip Calculator [Project]

print('Welcome to the tip calculator!')
bill_total = float(input('What was the total bill? $'))
tip = int(input('How much tip would you like to give? 10, 12, or 15? '))
people = int(input('How many people to split the bill? '))

tip_amount = bill_total * (tip / 100)
bill_with_tip = bill_total + tip_amount
split = bill_with_tip / people

# use round()
final_amount = round(split)

# for decimal places, use ' :.2f '
print(f"Each person should pay: ${final_amount:.2f}")