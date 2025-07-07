#Random Password Generator
import random
print("Welcome to the Random Password Generator!")
while True:
    length = int(input("Enter the length of the password: "))
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    symbols = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    num_letters = int(input("How many letters would you like in your password? "))
    num_numbers = int(input("How many numbers would you like in your password? "))
    num_symbols = int(input("How many symbols would you like in your password? "))
    if num_letters + num_numbers + num_symbols != length:
        print("The total of letters, numbers, and symbols must equal the length of the password.")
        continue
    if num_letters < 0 or num_numbers < 0 or num_symbols < 0:
        print("The number of letters, numbers, and symbols cannot be negative.")
        continue
    if length <= 0:
        print("The length of the password must be greater than zero.")
        continue
    password = ""
    for i in range(1,num_letters+1):
        random_letter = random.choice(letters)
        password += random_letter
    for i in range(1,num_numbers+1):
        random_number = random.choice(numbers)
        password += random_number
    for i in range(1,num_symbols+1):
        random_symbol = random.choice(symbols)
        password += random_symbol
    l = list(password)
    random.shuffle(l)
    password = ''.join(l)
    print("Your random password is:", password)
    again = input("Would you like to generate another password? (yes/no): ").strip().lower()
    if again != 'yes':
        print("Thank you for using the Random Password Generator!")
        break
