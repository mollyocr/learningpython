### 2018-11-13 mollyocr
#### practicepython.org exercise 9: guessing game one

## Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. (Hint: remember to use the user input lessons from the very first exercise)

## Extras:
  ## Keep the game going until the user types “exit”
  ## Keep track of how many guesses the user has taken, and when the game ends, print this out.

play = True
game_count = 0

print("I'm thinking of a number between 1 and 9. ")
while play:

    import random
    secret_number = random.randint(1,9)
    print(f"(Psst. For debugging purposes: the secret_number is {secret_number}.)")

    guess_attempts = 1
    solve_status = False

    while solve_status == False:

        # player_guess = None # or "" # Don't need this after rearranging to have only one input line
        player_guess = input("Take a guess! \n(Gimme a number.) >> ")

        if player_guess == "exit":
            play = False # or: break

        elif int(player_guess) == secret_number:
            solve_status = True
            game_count = game_count + 1
            print(f"You guessed my number! It took you {guess_attempts} guesses to guess my secret number! ")
            print(f"You've guessed {game_count} of my numbers now. ")

            play_again = input("Wanna play again? y/n \n >> ")
            if play_again == "y":
                # guess_attempts = 1 # Don't need this anymore since flipping the solve_status switch reroutes to reset this in the previous while loop.
                solve_status = True
            elif play_again == "n":
                play = False

        elif int(player_guess) > secret_number and int(player_guess) in range(1, 10):
            guess_attempts = guess_attempts + 1
            print("You guessed TOO HIGH. Try again. \n >> ")

        elif int(player_guess) < secret_number and int(player_guess) in range(1, 10):
            guess_attempts = guess_attempts + 1
            print("You guessed TOO LOW. Try again. \n >> ")

        else:
            while player_guess not in range(1, 10):
                print("Huh? Try again. (1 to 9 only please.) \n >> ")

print("Thanks for playing!")

#### DONE: OOPS YOU FORGOT about the "exit" loophole. ARGH. Go back and do this.

#### DONE: Something's broken!! Fix it -- AH. It's because the secret_number is changing between guesses because of its position in the while loop.
# Take a guess!
#  (Gimme a number.) >> 3
# You guessed TOO HIGH. Try again.
#  >>
# Take a guess!
#  (Gimme a number.) >> 2
# You guessed TOO LOW. Try again.

#### Put another while loop in, then
