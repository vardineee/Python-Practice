#Aks to enter the bill
#Ask to chose between  12,10,15 % to calculte total bill
#If the bill was $150.00, split between 5 people, with 12% tip.
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

print('Welcome tip calculator. ')
total_bill = int(input('What was the total bill? '))
precentage = int(input('What percentage tip would you like to give? 10, 12 or 15? '))
people = int(input('How many people to split the bill? '))

final_bill = round((total_bill*(precentage/100) +total_bill)/people, 2)

print(f"Ecah person should pay ${final_bill}")
