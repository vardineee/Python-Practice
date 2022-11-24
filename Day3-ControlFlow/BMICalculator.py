# #Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.
# It should tell them the interpretation of their BMI based on the BMI value.
# Under 18.5 they are underweight
# Over 18.5 but below 25 they have a normal weight
# Over 25 but below 30 they are slightly overweight
# Over 30 but below 35 they are obese
# Above 35 they are clinically obese.

height = float(input("Enter your height. "))
weight = float(input("Enter your weight. "))
bmi_rate = round(weight/height**2,2)

if bmi_rate < 18.5:
    print(f"Your BMI is {bmi_rate}, your are underweight.")
elif bmi<25:
    print(f"Your BMI is {bmi_rate}, you have a normal weight.")

elif bmi_rate < 30:
    print(f"Your BMI is {bmi_rate}, you are slightly overweight.")

elif bmi_rate < 35:
    print(f"Your BMI is {bmi_rate}, you are obese.")
else:
    print(f"Your BMI is {bmi_rate}, you are clinically obese.")
