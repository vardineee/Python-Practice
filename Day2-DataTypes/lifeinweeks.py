#Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.
#It will take your current age as the input and output a message with our time left in this format:
#You have x days, y weeks, and z months left.
your_age = int(input('Enter your age: '))
age = 90 - your_age
days =  age * 365
weeks = age * 52
months = age * 12

print(f"You have {days} days, {weeks} weeks, {months} months left.")
