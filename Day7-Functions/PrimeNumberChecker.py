

def prime_numer(number):
    is_prime = True
    for i in range(2,number):
        if number % i == 0:
            is_prime = False
    if is_prime == False:
            print(f" {number} is not a prime number")
    else:
        print(f" {number} is a prime number")


try_again = True
while try_again:

    number = int(input("Enter a number: "))
    prime_numer(number)
    should_continue = input("Try again.Type 'yes or 'no. ")
    if should_continue == 'no':
        try_again = False
        print("Goodbye")
