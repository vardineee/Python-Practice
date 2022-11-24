# You are going to write a program that tests the compatibility between two people.
# To work out the love score between two people:
# Take both people's names and check for the number of times the letters in the word TRUE occurs.
# Then check for the number of times the letters in the word LOVE occurs.
# Then combine these numbers to make a 2 digit number.
# For Love Scores less than 10 or greater than 90, the message should be:
# For Love Scores between 40 and 50, the message should be:
# Otherwise, the message will just be their score. e.g.:

name1 = input('Enter name: ').lower()
name2 = input('Enter Name: ').lower()
name = name1+name2
score_1 = 0
score_2 = 0

char=name.count('t')
print(f"T occures {char} times.")
score_1 += char
print(score_1)
char = name.count('r')
print(f"R occures {char} times")
score_1+=char
char = name.count('u')
print(f"U occures {char} times")
score_1+=char
char = name.count('e')
print(f"E occures {char} times")
score_1+=char
char = name.count('l')
print(f"L occures {char} times")
score_2+=char
char = name.count('o')
print(f"O occures {char} times")
score_2+=char
char = name.count('v')
print(f"V occures {char} times")
score_2+=char
char = name.count('e')
print(f"E occures {char} times")
score_2+=char

score =int( (str(score_1) + str(score_2)))

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score > 40 and score < 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
