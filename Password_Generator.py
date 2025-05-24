import random
import string

# Create lists of possible characters for the password:
letters = list(string.ascii_letters)    # All uppercase and lowercase English letters
numbers = list(string.digits)           # All digits 0-9
symbols = list(string.punctuation)      # Common punctuation and special symbols

print("Hello, and welcome to the password generator program.")

# Get user input for the number of each character type, with validation:
while True:
    try:
        # Ask the user how many letters, symbols, and numbers to include
        letters_input = int(input("Enter your number of letters (0-26): "))
        symbols_input = int(input("Enter your number of symbols (0-26): "))
        numbers_input = int(input("Enter your number of numbers (0-26): "))
        total = letters_input + symbols_input + numbers_input
        # Validate input: each value must be between 0 and 26, and at least one character in total
        if 0 <= letters_input <= 26 and 0 <= symbols_input <= 26 and 0 <= numbers_input <= 26 and total > 0:
            break
        else:
            print("Please enter a number between 0 and 26 for each field, and at least one character in total.")
    except ValueError:
        print("Please enter a valid integer between 0 and 26.")

# Build the password list by randomly selecting the requested number of characters from each category
# random.choices returns a list of k random elements (with possible repeats) from the given sequence
password = (
    random.choices(letters, k=letters_input) +
    random.choices(symbols, k=symbols_input) +
    random.choices(numbers, k=numbers_input)
)

# Shuffle the list to mix letters, symbols, and numbers randomly
random.shuffle(password)

# Join the list into a single string to form the final password
password_str = ''.join(password)

# Output the generated password and its length
print("Your generated password is:", password_str)
print(f"Password length: {len(password_str)}")
