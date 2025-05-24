# Loop until the user enters a valid integer greater than 0
while True:
    try:
        num_range = int(input("Enter the maximum range: "))
        if num_range >= 1:
            break  # Valid input, exit the loop
        else:
            print("Please enter a valid number greater than 0.")
    except ValueError:
        print("Please enter an integer only.")

# Loop through numbers from 1 up to and including num_range
for i in range(1, num_range + 1):
    output = ""  # Initialize output string for each number

    # If divisible by 3, add "Fizz" to output
    if i % 3 == 0:
        output += "Fizz"

    # If divisible by 5, add "Buzz" to output
    if i % 5 == 0:
        output += "Buzz"

    # Print output if it's not empty, otherwise print the number itself
    print(output or i)
