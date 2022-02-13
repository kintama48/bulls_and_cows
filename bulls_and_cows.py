import random


class BullsAndCows:
    def __init__(self, number_of_digits=4):     # init function initializes the int target value
        if number_of_digits == 1:               # by using the randint method of random.
                                                # number_of_digits represents the difficulty
                                                # and the range for the random number
                                                # to be picked
            self.target = str(random.randint(1, 9))
        else:
            self.target = str(random.randint(int('9' * (number_of_digits - 1)) + 1,
                                             int('9' * number_of_digits)))

    def get_target(self):                       # method to get the actual value
        return self.target

    def get_bulls_and_cows(self, guess):        # method to return bulls and cows in a certain
        bulls = 0                               # guess
        cows = 0
        for i in range(len(guess)):
            if guess[i] == self.target[i]:
                bulls += 1

            if guess[i] in self.target:
                cows += 1

        return bulls, cows - bulls

    @staticmethod
    def get_console_msg():          # welcome msg
        return "\n\n" \
               "             -------------------------------------\n" \
               "            |                                     |\n" \
               "            |       Welcome to Bulls & Cows       |\n" \
               "            |                                     |\n" \
               "             -------------------------------------\n\n" \
               "             --> Please specify the difficulty of\n" \
               "                 the game. A prompt will ask for \n" \
               "                 the difficulty.\n\n" \
               "                 1. Easy\n" \
               "                 2. Medium\n" \
               "                 3. Hard\n" \
               "\n           ->  You can quit anytime by entering 'Q'\n\n" \
               "                          Good luck!\n\n\n" \
               "             ->  Please enter the difficulty of \n" \
               "                 the game (1-3): " \


    @staticmethod
    def print_exit_msg():   # exit msg
        print("\n\n"
              "             -------------------------------------\n"
              "            |                                     |\n"
              "            |       Goodbye! See you soon!        |\n"
              "            |                                     |\n"
              "             -------------------------------------\n\n")

    @staticmethod
    def get_digits_and_guesses(difficulty):     # helper method to convert difficulty
                                                # to number_of_digits and the guesses
                                                # assosciated with each number_of_digits.
                                                # the values can be manipulated to add/remove
                                                # new levels of difficulty in the game

        while True:     # if invalid input, continue the loop
            if difficulty == "1":
                number_of_digits = 4
                number_of_guesses = 9
                return number_of_digits, number_of_guesses
            elif difficulty == "2":
                number_of_digits = 5
                number_of_guesses = 8
                return number_of_digits, number_of_guesses
            elif difficulty == "3":
                number_of_digits = 6
                number_of_guesses = 7
                return number_of_digits, number_of_guesses
            elif difficulty == 'Q' or difficulty == 'q':    # exit if 'Q' or 'q' entered
                return False, False
            else:
                difficulty = input("             --> Invalid difficulty. Please\n"
                                   "                 enter a NUMBER between\n"
                                   "                 1 and 3 or enter 'Q'\n"
                                   "                 to quit: ").rstrip().strip()
                continue


def start_game():
    difficulty = input(BullsAndCows.get_console_msg()).strip().rstrip()     # print welcome msg and get input
    if difficulty == 'q' or difficulty == 'Q':
        return False
    number_of_digits, number_of_guesses = BullsAndCows.get_digits_and_guesses(difficulty)  # get no of digits and guesses
                                                                                        # based on level of difficulty
    game = BullsAndCows(number_of_digits)   # initiate a BullsAndCows object and provide the no of digits to use

    # print(f'\nTarget: {game.target}\n')

    # maintaining a score board in a string variable will alleviate the need of using a for loop. new results are
    # concatenated in the string
    guess_board = "             -------------------------------------\n" \ 
                  "            | Turn |  Guess  |  Bulls  |   Cows   |\n" \
                  "             -------------------------------------\n"

    tries = number_of_guesses       # the number of tries the user will get according to the difficulty chosen
    guess = input("\n             --> Please enter your guess: ").rstrip().strip()

    while tries:        # loop ends when tries == 0
        try:
            if guess == 'Q' or guess == 'q':
                return False  # If 'Q' entered, print msg and exit the game

            elif guess == game.get_target():       # if correct value guessed the end the game
                tries -= 1
                bulls, cows = game.get_bulls_and_cows(guess)    # number of bulls and cows in the game
                guess_board += f"                {number_of_guesses - tries}  |  {guess}   |    {bulls}    |    {cows}  \n" \
                               "             -------------------------------------\n"   # add results to scoreboard
                print(guess_board)
                play_again = input(f"\n\n             --> Congratulations! You won.\n\n"    # win msg and ask to start
                                   f"             --> Would you like to start\n"            # new game
                                   f"                 a new game (Y or N)?: ").strip().rstrip()

                if play_again == 'Y' or play_again == 'y':
                    return True
                elif play_again == 'n' or play_again == 'N' or play_again == 'q' or play_again == 'Q':
                    return False

                while len(play_again) > 1 and play_again not in 'yYnNqQ':   # while invalid input, keep asking
                                                                            #  for valid input
                    play_again = input(f"\n             --> Please enter either 'Y', 'N', \n"
                                       f"                   or 'Q': \n").strip().rstrip()

            # if guessed number out of range, ask for it again
            elif int(guess) < (int('9' * (number_of_digits - 1)) + 1) or int(guess) > int('9' * number_of_digits):
                guess = input(f"             --> Please enter a number\n"
                              f"                 between {(int('9' * (number_of_digits - 1)) + 1)} "
                              f"and {('9' * number_of_digits)}: ").strip().rstrip()
                continue

            # if all if conditions fail then execute this code block which tells the user the bulls and cows in their
            # guess and then ask for input again
            tries -= 1
            bulls, cows = game.get_bulls_and_cows(guess)
            guess_board += f"                {number_of_guesses - tries}  |  {guess}   |    {bulls}    |    {cows}  \n" \
                           "             -------------------------------------\n"
            print(guess_board)
            guess = input("\n             --> Please enter your guess: ").rstrip().strip()
            continue

        # if user doesn't enter a number then program keeps asking for a valid input
        except ValueError:
            if guess == 'Q' or guess == 'q':
                return False  # If 'Q' entered, print msg and exit the game
            guess = input(f"             --> Please enter a NUMBER \n"
                          f"                 between {number_of_digits} digits\n"
                          f"                 or enter 'Q'\n"
                          f"                 to quit:  ").strip().rstrip()
            continue

    # if tries == 0 then that means user failed to guess the number so user is asked if they want to play again
    # then program exits
    play_again = input(f"\n             --> You lose. You ran out of tries :(\n\n"
                       f"             --> Would you like to start\n"
                       f"                 a new game (Y or N)?: ").strip().rstrip()
    while len(play_again) > 1 and play_again not in 'yYnNqQ':   # loop to check if user entered valid option
        play_again = input(f"\n             --> Please enter either 'Y', 'N', \n"
                           f"                   or 'Q': ").strip().rstrip()

    if play_again == 'Y' or play_again == 'y':
        return True
    elif play_again == 'n' or play_again == 'N' or play_again == 'q' or play_again == 'Q':
        return False
