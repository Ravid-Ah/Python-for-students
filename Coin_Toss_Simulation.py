import random

# Coin Toss Simulation Function

def coin_toss_simulation(sample_size):
    """
    Simulates tossing a coin 'sample_size' times.
    Returns the number of heads and tails.
    """
    heads_count = 0
    tails_count = 0
    for _ in range(sample_size):
        result = random.choice(["Heads", "Tails"])
        if result == "Heads":
            heads_count += 1
        else:
            tails_count += 1
    return heads_count, tails_count

# Input validation loop
while True:
    user_input = input("Please enter a sample size: ")
    try:
        number = int(user_input)
        if number > 0:
            break
        else:
            print("Please enter a number greater than 0.")
    except ValueError:
        print("Please enter an integer only.")

# Calling the function and printing results
heads, tails = coin_toss_simulation(number)

# Calculate percentages
heads_percent = heads / number * 100
# Round heads, and make tails the remainder to 100
heads_percent_rounded = round(heads_percent, 2)
tails_percent_rounded = round(100 - heads_percent_rounded, 2)

print(f"Sample size: {number}")
print(f"Heads: {heads}, Tails: {tails}")
print(f"Heads %: {heads_percent_rounded:.2f}, Tails %: {tails_percent_rounded:.2f}")
