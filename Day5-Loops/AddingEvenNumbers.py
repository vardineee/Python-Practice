#write a program tWat calculates the sum of all the even numbers from 1 to 100.
#i.e. 2 + 4 + 6 + 8 +10 ... + 98 + 100
#Important, there should only be 1 print statement in your console output. It should just print the final total and not every step of the calculation.

sum = 0
for number in range(0,101):
    if number % 2 == 0:
        sum +=number

print(f"The sum of even number from 1 to 100 is {sum}. " )
