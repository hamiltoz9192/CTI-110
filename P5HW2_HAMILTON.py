# This program creates a random guessing game between 1 and 100.
# July 8, 2018
# CTI-110 P5HW2 - Random Number Guessing Game
# ZACHARY HAMILTON
#

def play_game():
    import random
    guess = int(input('I am thinking of a number between 1 and 100, what is it?: '))
    random = random.randrange(1, 100)
    guesses_remaining = 8
    while random != guess:
        if random > guess:
            print('Too low, try again')
            guesses_remaining = guesses_remaining - 1
            print('Guesses remaining: ', guesses_remaining)
            guess = int(input('Guess again: '))
        else:
            print('Too high, try again')
            guesses_remaining = guesses_remaining - 1
            print('Guesses remaining: ', guesses_remaining)
            guess = int(input('Guess again: '))
        if guesses_remaining == 0:
            print('Ran out of attempts. The winning number is: ', random)
    print('That is correct, you have guessed the number I was thinking!')
    def main():
        again = 'y'
        while again == 'y' or again == 'Y':
            again = input('Would you like to play again?: ')
            import random
            guess = int(input('I am thinking of a number between 1 and 100, what is it?: '))
            random = random.randrange(1, 100)
            guesses_remaining = 8
            while random != guess:
                if random > guess:
                    print('Too low, try again')
                    guesses_remaining = guesses_remaining - 1
                    print('Guesses remaining: ', guesses_remaining)
                    guess = int(input('Guess again: '))
                else:
                    print('Too high, try again')
                    guesses_remaining = guesses_remaining - 1
                    print('Guesses remaining: ', guesses_remaining)
                    guess = int(input('Guess again: '))
                if guesses_remaining == 0:
                    print('Ran out of attempts. The winning number is: ', random)
            print('That is correct, you have guessed the number I was thinking!')
    main()
play_game()
