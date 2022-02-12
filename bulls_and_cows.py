import random


class BullsAndCows:
    def __init__(self, number_of_digits=4):
        if number_of_digits == 1:
            self.target = str(random.randint(1, 9))
        else:
            self.target = str(random.randint(int('9' * (number_of_digits - 1)) + 1,
                                             int('9' * number_of_digits)))

    def get_target(self):
        return self.target

    def get_bulls_and_cows(self, guess):
        bulls = 0
        cows = 0
        for i in range(len(guess)):
            if guess[i] == self.target[i]:
                bulls += 1

            if guess[i] in self.target:
                cows += 1

        return bulls, cows - bulls

    @staticmethod
    def get_console_msg():
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
    def print_exit_msg():
        print("\n\n"
              "             -------------------------------------\n"
              "            |                                     |\n"
              "            |       Goodbye! See you soon!        |\n"
              "            |                                     |\n"
              "             -------------------------------------\n\n")

    @staticmethod
    def get_digits_and_guesses(difficulty):
        while True:
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
            else:
                difficulty = input("             --> Invalid difficulty. Please\n"
                                   "                 enter a NUMBER between\n"
                                   "                 1 to 3 or enter 'Q'\n"
                                   "                 to quit: ").rstrip().strip()
                if difficulty == 'Q' or difficulty == 'q':
                    return False, False
                continue


def start_game():
    difficulty = input(BullsAndCows.get_console_msg())
    number_of_digits, number_of_guesses = BullsAndCows.get_digits_and_guesses(difficulty)
    game = BullsAndCows(number_of_digits)

    # print(f'\nTarget: {game.target}\n')
    
    guess_board = "             -------------------------------------\n" \
                  "            | Turn |  Guess  |  Bulls  |   Cows   |\n" \
                  "             -------------------------------------\n"
    tries = number_of_guesses
    guess = input("\n             --> Please enter your guess: ").rstrip().strip()

    while tries:
        try:
            if guess == 'Q' or guess == 'q':
                return False  # If 'Q' entered, print msg and exit the game

            elif guess == game.get_target():
                tries -= 1
                bulls, cows = game.get_bulls_and_cows(guess)
                guess_board += f"                {number_of_guesses - tries}  |  {guess}   |    {bulls}    |    {cows}  \n" \
                               "             -------------------------------------\n"
                print(guess_board)
                play_again = input(f"\n\n             --> Congratulations! You won.\n\n"
                                   f"             --> Would you like to start\n"
                                   f"                 a new game (Y or N)?: ").strip().rstrip()

                if play_again == 'Y' or play_again == 'y':
                    return True
                elif play_again in 'nN' or play_again in 'qQ':
                    return False

                while play_again not in 'yYnNqQ':
                    play_again = input(f"\n             --> Please enter either 'Y', 'N', \n"
                                       f"                   or 'Q': \n").strip().rstrip()

            elif int(guess) < (int('9' * (number_of_digits - 1)) + 1) or int(guess) > int('9' * number_of_digits):
                guess = input(f"             --> Please enter a number\n"
                              f"                 between {(int('9' * (number_of_digits - 1)) + 1)} "
                              f"and {('9' * number_of_digits)}: ")
                continue

            tries -= 1
            bulls, cows = game.get_bulls_and_cows(guess)
            guess_board += f"                {number_of_guesses - tries}  |  {guess}   |    {bulls}    |    {cows}  \n" \
                           "             -------------------------------------\n"
            print(guess_board)
            guess = input("\n             --> Please enter your guess: ").rstrip().strip()
            continue

        except ValueError:
            guess = input(f"             --> Please enter a NUMBER \n"
                          f"                 between {number_of_digits} digits\n"
                          f"                 or enter 'Q'\n"
                          f"                 to quit:  ")
            continue
    else:
        play_again = input(f"\n             --> You ran out of tries :(\n\n"
                           f"             --> Would you like to start\n"
                           f"                 a new game (Y or N)?: ").strip().rstrip()
        while play_again not in 'yYnNqQ':
            play_again = input(f"\n             --> Please enter either 'Y', 'N', \n"
                               f"                   or 'Q': ").strip().rstrip()

        if play_again == 'Y' or play_again == 'y':
            return True
        elif play_again in 'nN' or play_again in 'qQ':
            return False
