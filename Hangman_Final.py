import random
import os

# Print the current working directory and script location for debugging
print("Current working directory:", os.getcwd())
print("Script location:", os.path.abspath(__file__))

def load_words_from_file(filename):
    """
    Loads words from a text file located in the same directory as this script.
    Each word should be on a separate line in the file.
    Returns a list of cleaned, lowercase words.
    """
    # Get the directory where the script is located
    base_dir = os.path.dirname(os.path.abspath(__file__))
    # Build the full path to the words.txt file
    file_path = os.path.join(base_dir, filename)
    print("Looking for words.txt at:", file_path)  # For debugging
    with open(file_path, "r", encoding="utf-8") as file:
        # Read each line, strip whitespace, convert to lowercase, and ignore empty lines
        return [line.strip().lower() for line in file if line.strip()]

def play_hangman(word_list):
    """
    Main function to play a single game of Hangman.
    Receives a list of possible words to choose from.
    """
    # Randomly select a word from the list
    chosen_word = random.choice(word_list)
    # Placeholder for displaying current progress (e.g., "_ _ _ _")
    placeholder = ["_"] * len(chosen_word)
    # Number of lives the player has at the start
    lives = 5
    # Set to keep track of all guessed letters
    guessed_letters = set()

    # Game loop: continue until player runs out of lives or guesses the word
    while lives > 0 and "_" in placeholder:
        print("\nWord:", " ".join(placeholder))
        print("Guessed letters:", " ".join(sorted(guessed_letters)))
        print("Lives left:", lives)

        # Get input from the player and validate it
        guess_letter = input("Guess a letter: ").lower()
        if len(guess_letter) != 1 or not guess_letter.isalpha():
            print("Please enter a single valid letter.")
            continue
        if guess_letter in guessed_letters:
            print("You already guessed that letter. Try a different one.")
            continue

        # Add the guessed letter to the set
        guessed_letters.add(guess_letter)

        # Check if the guessed letter is in the chosen word
        if guess_letter in chosen_word:
            print("Right guess!")
            # Reveal all occurrences of the guessed letter in the placeholder
            for i, letter in enumerate(chosen_word):
                if guess_letter == letter:
                    placeholder[i] = letter
        else:
            print("Wrong guess!")
            lives -= 1  # Deduct a life for a wrong guess

    # Game over: check if the player won or lost
    if "_" not in placeholder:
        print("Congratulations! You won! The word was:", chosen_word)
    else:
        print("Game over! The word was:", chosen_word)

def ask_to_play():
    """
    Asks the player if they want to play another game.
    Returns True if yes, False if no.
    """
    while True:
        answer = input("Do you want to play a new game? (y/n): ").strip().lower()
        if answer == 'y':
            return True
        elif answer == 'n':
            print("Goodbye!")
            return False
        else:
            print("Please enter 'y' for yes or 'n' for no.")

if __name__ == "__main__":
    # Load the word list from a file at the start of the program
    word_list = load_words_from_file("words.txt")
    # Check if the word list is empty or file wasn't found
    if not word_list:
        print("Word list is empty or file not found. Please check words.txt.")
    else:
        # Loop to allow playing multiple games
        while ask_to_play():
            play_hangman(word_list)