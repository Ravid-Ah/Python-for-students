import random

def toss_coin():
    heads = ('''
      ╔════════╗)
     ╔╝ ░░░▒▒▓ ╚╗
    ╔╝ ░░░░▒▒▓▓ ╚╗
    ║ ░░░HEAD▒▓▓ ║
    ╚╗ ░░░▒▒▒▓▓ ╔╝
     ╚╗ ░░░▒▒▓ ╔╝
      ╚════════╝
    ''')
    tails = ('''
      ╔════════╗
     ╔╝ ░░░▒▒▓ ╚╗
    ╔╝ ░░░░▒▒▓▓ ╚╗
    ║ ░░░TAIL▒▓▓ ║
    ╚╗ ░░░▒▒▒▓▓ ╔╝
     ╚╗ ░░░▒▒▓ ╔╝
      ╚════════╝
    ''')
    result = random.choice([("Heads", heads), ("Tails", tails)])
    print(result[1])
    print(f"Result: {result[0]}")

print("Hello and welcome to the coin toss program, let's toss a coin.")
while True:
    user_input = input('Are you ready? Please press "Enter" to toss!')
    if user_input == "":
        toss_coin()
        break
    else:
        print('Please just press "Enter" to continue, nothing else!')
