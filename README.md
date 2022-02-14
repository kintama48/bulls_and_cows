# Abdullah Baig  | 231485698
# Hamza Asaad   | 231450993
___________________________________________________________

## Bulls And Cows

### Time Complexity Analysis:

Our time complexity analysis assumes complexity across 1 game. To begin, our driver runs the _start_game()_ function of our _BullAndCows_ class.

Our first action is to take the difficulty input for the game, the error handling and parsing of this we will assume to take constant time.

Next, our game object is created which generates and initializes our _self.target_ attribute for the game. We again assume this will take constant time.

Our while loop is started based on how many guesses each difficulty allows therefore the number of tries for our while loop

Our _‘while tries - loop’_ is where the game is centred at, it takes an input or more specifically a guess and runs several checks. The user input can either be ‘ _Q’_ to quit the game or have input errors such as not being a digit. We will consider these to be of constant time and it does not affect the actual complexity of the game.

The next two checks are whether the guess is equivalent to the _target_. This will, most likely, not be the worst-case scenario as except for on the last try left the passing of this condition will break our loop and not lead to a worst-case time complexity scenario.

This brings us to the last case where none of the checks passes and our _get_bulls_and_cows()_ function will be called which will run a single for loop and iterate over the input digits and calculate the number of bulls and cows. This for loop will be of _‘N’_ time complexity where _‘N’_ is the _number_of_digits_ our game is checking for; _number_of_digits_ can vary and can be given any value to increase the difficulty of the game.

```
N will dominate the constant time complexity of each iteration of our ‘tries while loop', therefore the time complexity will be O(N)
```
Lastly, our _‘try while loop’_ can iterate for an infinite number of times given incorrect user input in the worst-case scenario; we will not be considering this case. What we will consider is the user will input the correct input on each iteration and in a worst-case scenario, no input for all tries matches the target digits of the game in this case our while loop runs a total of _“T”_ times, where “T” is the number of tries which is calculated using the selected difficulty of the game; _‘number of tries’_ can also be modified to increase/decrease the difficulty of our game.

*_Therefore:_*
```
considering all of the assumptions stated above, O(TN) is the worst-case time complexity of our game
```

### Key:

```
T = number of tries allowed based on the selected difficulty
N = number of digits game is checking for based on the selected difficulty
```

