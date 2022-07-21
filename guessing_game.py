import random
import sys
import statistics
total_attempts = []

# use f-strings to format strings.

def call_statistics(list):
    tot_att = sum(list)
    mean = statistics.mean(list)
    median = statistics.median(list)
    mode = statistics.mode(list)
    print(f"Your total number of attempts was {tot_att}")
    print(f"Your mean number of attempts per game was {mean}")
    print(f"Your median number of attemtps per game was {median}")
    print(f"Your mode number of attemtps per game was {mode}")

def start_game(game_attempts):
    attempts = 0
    # A random number should be chosen that is within the range of 1 - 100.
    random_num = random.randint(1, 100)
    print(random_num)
    run = True
    # As a player of the game, I should see some kind of text header, welcome, or game intro message
    print("Hello! Welcome to the random number game!")
    try:
        while run:
            guess = int(input("Please guess a whole number between 1 and 100:  "))
            # continuously prompted for a guess until I get it right.
            # I should be told if my answer is higher or lower 
            # If my guess is outside the guessing range I should be told to try again.
            if guess < 1 or guess > 100:
                print("You're number is outside the range, try again!")
                attempts += 1
                continue
            elif guess > random_num:
                print("It's lower, try again!")
                attempts += 1
                continue
            elif guess < random_num:
                print("It's higher, try again!")
                attempts += 1
                continue
            elif guess == random_num:
                attempts += 1
                # save the player’s number of attempts at guessing to a list.
                game_attempts.append(attempts)
                print(f"You got it! Number of attempts: {attempts}")
                # show the current best score
                best_score = min(game_attempts)
                print(f"The current best score is {best_score}")
                # I should be prompted if I would like to play again.
                cont_game = input("Would you like to play again? Yes or No  ")
                if cont_game.upper() == "YES":
                    start_game(game_attempts)
                    continue
                elif cont_game.upper() == "NO":
                    # ending message is shown to the player.
                    print("~Okay, thanks for playing~")
                    call_statistics(game_attempts)
                    exit()
                #catch possible errors in input
                else:
                    print("Invalid response, please type 'yes' or 'no'")
                    exit()
    #catch possible errors in input
    except ValueError:
        print("Invalid response, please type a whole number from 1-100")

start_game(total_attempts)
