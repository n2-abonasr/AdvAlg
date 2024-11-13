from itertools import product

# Define sets
capital_letters = ['A', 'B', 'C', 'D', 'E']
lowercase_letters = ['a', 'b', 'c', 'd', 'e']
digits = ['1', '2', '3', '4', '5']
special_symbols = ['$', '&', '%']

# Function to check if a password is valid
def is_valid(password):
    has_capital = any(char in capital_letters for char in password)
    has_lowercase = any(char in lowercase_letters for char in password)
    has_digit = any(char in digits for char in password)
    has_special = any(char in special_symbols for char in password)
    starts_with_letter = password[0] in capital_letters + lowercase_letters
    capital_count = sum(char in capital_letters for char in password)
    special_count = sum(char in special_symbols for char in password)
    
    return (has_capital and has_lowercase and has_digit and has_special and 
            starts_with_letter and capital_count <= 2 and special_count <= 2)

# Loop until user chooses to exit
while True:
    # Read the length from the console
    length = int(input("Enter the password length: "))

    # Generate all possible passwords
    all_passwords = product(capital_letters + lowercase_letters + digits + special_symbols, repeat=length)

    # Filter the valid passwords
    valid_passwords = [password for password in all_passwords if is_valid(password)]

    # Print the valid passwords with indices
    for i, password in enumerate(valid_passwords, start=1):
        print(f"{i} {''.join(password)}")
    
