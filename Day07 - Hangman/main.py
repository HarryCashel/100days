"""Program that plays hangman with user"""

# imports
import random
from words import easy, medium, hard


# function to select difficulty
def select_difficulty():
    difficulty = input("Select difficulty = 'easy', 'medium' or 'hard': ")

    if difficulty.lower() == 'easy':
        word_list = easy
    elif difficulty.lower() == 'medium':
        word_list = medium
    elif difficulty.lower() == 'hard':
        word_list = hard
    return word_list


# function to continually run select difficulty until user correctly enters difficulty
def run_selection():

    try:
        return select_difficulty()
    except UnboundLocalError:
        print("Please enter 'easy', 'medium', or 'hard'.")
        run_selection()


# generate a random word from stored lists
answer = random.choice(run_selection())
print(answer)

# Create a list of the chosen word

# Option 1
# word = [i for i in answer]
# print(word)

# Option 2
word = list(answer)
# print(word)

# Create a list that displays '_' for each letter
display = []
for i in word:
    display.append("_")
# print(display)

# Set lives for player and condition that the game is won to False
lives = 5
game_not_won = True

# Allow user to guess for letters - While lives > 0
# Continue to ask user for a letter until lives are gone or word is guessed
while lives > 0 and game_not_won:
    # Show number of letters in mystery word
    print(display)
    # Ask user for a letter!
    guess = (input("Guess a letter! ")).lower()

    # Provide user option to guess the word
    if guess == answer:
        display = word
        game_not_won = False

    # Check if the user has already guessed this letter
    # Skip the rest of the loop if True
    elif guess in display:
        print(f"You have already guessed {guess}")
        continue

    # Check if user's guess is in the mystery word
    # Show user they have guessed correctly
    # Update the display list with the correct letter in the correct place
    elif guess in word:
    #     print("Yes")
    #     count = 0
    #     for i in word:
    #         if guess == i:
    #             display[count] = guess
    #         count += 1

    # Alternate way to code populating the display - I think this is cleaner

        for pos in range(len(word)):
            if word[pos] == guess:
                display[pos] = guess

    # If user guess not in the mystery word - remove a life
    # Will end the while loop if lives = 0
    elif guess not in word:
        if lives == 1:
            print("No lives left. Game Over")
            break
        lives -= 1
        print("Wrong! You lost a life")

    # If all letters have been guessed - Player wins and the loops ends
    if display == word:
        game_not_won = False
        print("You win!")
        print(f"The word was {''.join(display)}")