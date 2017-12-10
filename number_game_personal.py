import random

def play_again():
    play_again = input("Do you want to play again? Y/n")
    if play_again.lower() != 'n':
        count = 0
        game()
    else:
        print("Bye!")

def game():
    # generate a random number between 1 and 10
    secret_number = random.randint(1,10)
    # store the users gueses
    guesses = []
    # keep track of the number of times the game is played
    count = 0
    # create a game loop
    while len(guesses) < 5:
        # keep count of plays before 5 turns are up
        count = count + 1
        cheat = 911
        cheat_count = 0
        try:
            # convert input into an int and keep it as an int
            guess = int(input("Guess a number between 1 and 10: "))
            # throws an error if the users inputs anything other than an int
        except ValueError:
            print("Please guess a number!")
        else:
            # compare guess to secret number
            if guess == secret_number:
                if count == 1:
                    print("Congrats the secret number is {} you got it after {} try! You must be psychic!".format(secret_number,count))
                    play_again()

                elif count == 2:
                    print("Not bad the secret number is {}! You got it after {} tries!".format(secret_number,count))
                    play_again()

                elif count == 3:
                    print("Your alright kid! The secret number is {}! You got it after {} tries!".format(secret_number,count))

                    play_again()

                else:
                    print("Good but too late!")

            elif guess == 911:
                new_guess = [0]
                for new in new_guess:
                    new = new_guess
                    new_guess = 1
                    cheat_count = cheat_count + 1
                    print("clever you found a cheat code {}! {} is the secret number!".format(cheat,secret_number))
            elif guess < secret_number:
                print("my number is higher than {}!".format(guess))
            elif guess > secret_number:
                print("my number is lower than {}!".format(guess))
            guesses.append(guess)
    #after the the while loop is complete it'll print below
    else:
        # game over and gives option to play game again if yes calls to play if not it'll break
        print("Too many tries! The number was {}! Game over!".format(secret_number))

    play_again()
game()
