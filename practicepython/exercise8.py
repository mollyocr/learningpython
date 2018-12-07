### 2018-11-13 mollyocr
#### practicepython.org exercise 8: rock paper scissors

## Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

## Remember the rules:
  ## Rock beats scissors
  ## Scissors beats paper
  ## Paper beats rock

play = True
player_score = 0
computer_score = 0

while play == True:

    player_throw = int(input("Let's play Rock-Paper-Scissors! What's your throw?? \n 1 ROCK \n 2 PAPER \n 3 SCISSORS \n (Gimme a number.) \n >> "))

    import random
    computer_throw = random.randint(1,3)

    if int(player_throw) == 1:
        print ("Your throw: ROCK")
    elif int(player_throw) == 2:
        print ("Your throw: PAPER")
    elif int(player_throw) == 3:
        print ("Your throw: SCISSORS")
    else:
        while player_throw not in [1, 2, 3]:
            print (f"Your throw is invalid: {player_throw}")
            player_throw = int(input("Huh? Try again. (1, 2, or 3 please.) \n >> "))
            # print (f"Your throw is still invalid: {player_throw}")
            if int(player_throw) == 1:
                print ("Your throw: ROCK")
                # break
            elif int(player_throw) == 2:
                print ("Your throw: PAPER")
                # break
            elif int(player_throw) == 3:
                print ("Your throw: SCISSORS")
                # break

    if computer_throw == 1:
        print ("My throw: ROCK")
    elif computer_throw == 2:
        print ("My throw: PAPER")
    elif computer_throw == 3:
        print ("My throw: SCISSORS")

    if player_throw == computer_throw:
        print ("It's a tie!")
    elif player_throw == 1 and computer_throw == 2:
        print ("My PAPER covers your ROCK. You lose! ")
        computer_score = computer_score + 1
    elif player_throw == 1 and computer_throw == 3:
        print ("Your ROCK beats my SCISSORS. You win! ")
        player_score = player_score + 1
    elif player_throw == 2 and computer_throw == 1:
        print ("Your PAPER covers my ROCK. You win! ")
        player_score = player_score + 1
    elif player_throw == 2 and computer_throw == 3:
        print ("My SCISSORS beats your PAPER. You lose! ")
        computer_score = computer_score + 1
    elif player_throw == 3 and computer_throw == 1:
        print ("My ROCK beats your SCISSORS. You lose! ")
        computer_score = computer_score + 1
    elif player_throw == 3 and computer_throw == 2:
        print ("Your SCISSORS beats my PAPER. You win! ")
        player_score = player_score + 1

    #### Surely there's a way to smash all these if's into one if instead of three; I'm just not really in the mood.
    #### QUESTION for discussion: Generally speaking, how important is super streamlined efficient code compared to neat little reusable building blocks?

    print (f"Here are our scores. \n You: {player_score} \n Me: {computer_score} ")

    play_again = input("Wanna play again? y/n \n >> ")

    if play_again == "y":
        play = True
        continue
    elif play_again == "n":
        play = False
        print ("Ok, maybe later. Later, dude!")
