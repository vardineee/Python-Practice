# Based on a user's order, work out their final bill.
# Small Pizza: $15
# Medium Pizza: $20
# Large Pizza: $25
# Pepperoni for Small Pizza: +$2
# Pepperoni for Medium or Large Pizza: +$3
# Extra cheese for any size pizza: + $1

pizza = input('Enter pizza size. S, M or L. ')
add_pepperoni = input('Do you want Pepperoni? Type Yes or No. ')
add_cheese = input('Do you want extra cheese? Type Yes or No. ')
bill = 0

if pizza == 'S':
    bill+=15
    if  add_pepperoni =='Y':
        bill+=2

elif pizza == 'M':
    bill+=20
    if  add_pepperoni =='Y':
        bill+=3

else:
    bill +=25
    if  add_pepperoni =='Y':
        bill+=3

if add_cheese == 'Y':
    bill+=1
    
print(f"Your final bill is {bill}")
