#Random Password Generator
import random
print("Welcome to the Random Password Generator!")
while True:
    length = int(input("Enter the length of the password: ")) # User input for password length
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ" # Letters to choose from
    numbers = "0123456789" # Numbers to choose from
    symbols = "!@#$%^&*()_+-=[]{}|;:,.<>?" # Symbols to choose from
    #input for number of letters, numbers, and symbols
    num_letters = int(input("How many letters would you like in your password? "))
    num_numbers = int(input("How many numbers would you like in your password? "))
    num_symbols = int(input("How many symbols would you like in your password? "))
    # Check if the total of letters, numbers, and symbols equals the length of the password
    if num_letters + num_numbers + num_symbols != length:
        print("The total of letters, numbers, and symbols must equal the length of the password.")
        continue
    # Check if the number of letters, numbers, and symbols are valid
    if num_letters < 0 or num_numbers < 0 or num_symbols < 0:
        print("The number of letters, numbers, and symbols cannot be negative.")
        continue
    # Check if the length is greater than zero
    if length <= 0:
        print("The length of the password must be greater than zero.")
        continue
    password = ""
    # Generate the password
    for i in range(1,num_letters+1):
        random_letter = random.choice(letters)
        password += random_letter
    for i in range(1,num_numbers+1):
        random_number = random.choice(numbers)
        password += random_number
    for i in range(1,num_symbols+1):
        random_symbol = random.choice(symbols)
        password += random_symbol
    # Shuffle the password to make it more random
    l = list(password)
    random.shuffle(l)
    password = ''.join(l)
    print("Your random password is:", password)
    # Ask the user if they want to generate another password
    again = input("Would you like to generate another password? (yes/no): ").strip().lower()
    if again != 'yes':
        print("Thank you for using the Random Password Generator!")
        break
