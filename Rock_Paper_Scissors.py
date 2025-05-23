import random

# Welcome Message & input
print("Welcome to the Rock, Paper, Scissors game!")
player_1 = input("What do you choose? Type 0 for Rock, "
                     "1 for Paper or 2 for Scissors.\n")

# Verify input & convert str to int
if player_1 not in ["0", "1", "2"]:
    print("Invalid input, please try again.")
    exit()
else:
    player_1 = int(player_1)

# Initialize CPU choice
player_cpu = random.randint(0,2)

# Images
rock = ('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')

paper = ('''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''')

scissors = ('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')

# Images --> List & Printing choices
image = [rock, paper, scissors]
print(image[player_1])
print(image[player_cpu])

# If == tie
# if (P1-CPU) modulo 1 then P1 wins
    # Example 1: Paper (1) - Rock (0) = 1, 1%3 = 1

    # Example 2: Rock (0) - Scissors (2) = -2, (-2)%3 -->
    # the closest smaller value is (-3), and (-2)-(-3) = 1,
    # hence remainder 1

# if modulo 2 (else) CPU wins
    #Same reasoning

if player_1 == player_cpu:
    print("It's a tie!")
elif (player_1 - player_cpu) % 3 == 1:
    print("You Win!")
else:
    print("You Lose!")