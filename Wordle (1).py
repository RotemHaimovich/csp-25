"""
  WORD GUESSER 
  This is a game like wordle where the player guesses a
  secret 5 letter word. Each guess gets color coded feedback:
  green = right letter, right spot
  yellow = right letter, wrong spot
  gray = letter not in word
  Players have 6 attempts.
"""

import random


# data: The list 'word_bank' stores all possible secret words.
# this list is used to randomly select a secret word each game
word_bank = [
    "crane", "slate", "audio", "raise", "stare",
    "snare", "trace", "crate", "irate", "arose",
    "piano", "flair", "blaze", "glare", "shale",
    "groan", "clamp", "flint", "brisk", "swift",
    "plumb", "crisp", "storm", "blend", "frost",
    "grasp", "silas", "dwarf", "trees", "glyph",
    "chunk", "proxy", "ethic", "quest", "joust",
    "knave", "quirk", "pixel", "depot", "ultra",
]

# abstraction: get_feedback is a helper procedure used multiple times inside run_game. It hides the logic of comparing a guess to the secret word and returning color codes.
# input: guess (str), secret (str)
# output: a list of 5 strings. Each is "green", "yellow", or "gray"
def get_feedback(guess, secret):
    feedback = []  # list to store result for each letter
    secret_letters = list(secret)

    # iteration: loop through every letter position
    for i in range(len(guess)):

        # selection: check if letter is correct position
        if guess[i] == secret[i]:
            feedback.append("green")
            secret_letters[i] = None   # mark as used

        # selection: check if letter exists but is in wrong spot
        elif guess[i] in secret_letters:
            feedback.append("yellow")
            secret_letters[secret_letters.index(guess[i])] = None

        # selection: letter is not in the word at all
        else:
            feedback.append("gray")

    return feedback # returns a list of color strings


# abstration: display_guess is called once per guess inside run_game. It handles all the printing logic so run_game stays clean. There is no return value (command procedure).
# input: guess (str), feedback (list of color strings)
def display_guess(guess, feedback):
    # iteration: loop through each letter and its color code
    colored = ""
    for i in range(len(guess)):
        letter = guess[i].upper()

        # selection: pick display style based on feedback color
        if feedback[i] == "green":
            colored += f"\033[42m {letter} \033[0m"   # green background
        elif feedback[i] == "yellow":
            colored += f"\033[43m {letter} \033[0m"   # yellow background
        else:
            colored += f"\033[100m {letter} \033[0m"  # gray background

    print("  " + colored)


# abstraction: get_difficulty lets the user pick a difficulty level which controls how many words are in play. Called once at the start of run_game and returns the filtered word pool.
# input: none   output: filtered list of words (list)
def get_difficulty():
    print("\n  Choose a difficulty:")
    print("  [1] Easy: common words only (first 15)")
    print("  [2] MediumL wider word pool (first 25)")
    print("  [3] Hard full word bank (all 40)\n")

    choice = input("  Enter 1, 2, or 3: ").strip()

    # return a slice of word_bank based on choice
    # This shows how the list data is used toward the program's purpose
    if choice == "1":
        return word_bank[:15] # easy: slice of word_bank list
    elif choice == "3":
        return word_bank # hard: full word_bank list
    else:
        return word_bank[:25] # medium: default


# main procedure: run_game contains the full game loop.
#   includes:
#   sequence: setup, loop, result 
#   selection:  if/elif/else for win/lose/invalid guess checks
#   iteration:  while loop runs up to MAX_GUESSES times
# input: none   output: returns True if player won, False if lost
def run_game():
    MAX_GUESSES = 6
    WORD_LENGTH = 5

    # sequencing step 1: get difficulty and pick secret word
    pool = get_difficulty()  # calls get_difficulty abstraction
    secret = random.choice(pool)  # picks random word from the list

    guesses_used = 0
    guess_history = []  # list storing all guesses this game

    print("  WORD GUESSER  |  Guess the 5 letter word!")
    print("  You have 6 tries. Good luck!")

    # sequencing step 2: main guess loop
    # iteration: repeat until player wins or runs out of guesses
    while guesses_used < MAX_GUESSES:
        remaining = MAX_GUESSES - guesses_used
        guess = input(f"  Guess {guesses_used + 1}/6 ({remaining} left): ").strip().lower()

        # selection: validate the guess before processing it
        if len(guess) != WORD_LENGTH:
            print(f"  ✗ Must be exactly {WORD_LENGTH} letters. Try again.\n")
            continue   # skip rest of loop, don't count as a guess

        if not guess.isalpha():
            print("  ✗ Letters only, no numbers or symbols.\n")
            continue

        # sequencing step 3: process the valid guess
        guesses_used += 1
        guess_history.append(guess)   # store guess in the history list

        feedback = get_feedback(guess, secret)   # call get_feedback abstraction
        display_guess(guess, feedback)   # call display_guess abstraction
        print()

        # selection: check if the player won
        if guess == secret:
            print(f"  🎉 You got it in {guesses_used} guess{'es' if guesses_used > 1 else ''}!\n")
            return True   # return win result

    # sequencing step 4: if loop ends without win, player lost
    print(f"  💀 Out of guesses! The word was: {secret.upper()}\n")
    return False   # return lose result

# handles replay loop so player can keep playing without restarting the script. Uses the return value of run_game.
def main():
    print("  Welcome to WORD GUESSER!")

    wins = 0
    losses = 0
    games_played = 0

    # iteration: keeps running until player quits
    while True:
        won = run_game()   # run one full game, get result
        games_played += 1

        # selection: update win/loss counter based on result
        if won:
            wins += 1
        else:
            losses += 1

        # show stats
        print(f"  Stats: {games_played} played | {wins} wins | {losses} losses")
        print(f"  Win rate: {round(wins / games_played * 100)}%\n")

        again = input("  Play again? (yes / no): ").strip().lower()

        # selection: check if player wants to keep going
        if again != "yes":
            print("\n  Thanks for playing! Final stats:")
            print(f"  Games: {games_played} | Wins: {wins} | Losses: {losses}")
            print(f"  Win rate: {round(wins / games_played * 100)}%")
            print("\n  Goodbye!\n")
            break


# Run the program
main()
