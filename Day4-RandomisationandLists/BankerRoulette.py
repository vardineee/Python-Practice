# You are going to write a program that will select a random name from a list of names. The person selected will have to pay for everybody's food bill.
import random
name_string = input("Give me everybody's names, seperated by a comma.")
names = name_string.split(",")
number = len(names)-1

random_choice = random.randint(0, number)
print(f"The bill will pay {names[random_choice]}")
