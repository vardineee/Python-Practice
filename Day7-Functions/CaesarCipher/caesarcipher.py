from alphabet import alphabet
from art import logo

print(logo)


def caesar(direction, message, shift_number):
    new_message = ""
    for char in message:
        if char in alphabet:
            position = alphabet.index(char)
            if direction == "encode":
                new_postition = position + shift_number
                new_message +=alphabet[new_postition]
            elif direction =="decode":
                new_postition = position - shift_number
                new_message +=alphabet[new_postition]
        else:
            new_message +=char
    print(f"The {direction} is {new_message}.")

try_again =True
while try_again:

    direction = input("Type 'encode', to encrypt type 'decode' to decrypt:\n ").lower()
    message = input("Type your message:\n ")
    shift = int(input("Type the shift number: \n"))
    shift_number = shift % 26
    caesar(direction, message,shift_number)

    result = input("Type 'Yes', if you want to go again. Otherwise type 'No'. ").lower()
    if result == 'no':
        try_again = False
        print("GoodBye")
