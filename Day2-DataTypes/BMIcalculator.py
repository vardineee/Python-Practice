#Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.
#The BMI is a measure of someone's weight taking into account their height. e.g. If a tall person and a short person both weigh the same amount, the short person is usually more overweight.
#The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):

weight = float(input('Enter your weight in kg.\n'))
height = float(input('Enter your height in m.\n'))
person_BMI = int(weight/height**2)
print(f'Person Body Mass Index is {person_BMI}')
