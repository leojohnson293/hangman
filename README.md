# Hangman
> Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts. This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. The purpose of this project is the learn the fundamentals of python.

## Milestone 1
---
Firstly in python, a list with different fruits was created. Then using the random module, a variable called `word` will randomly choose one of the fruits using the `choose` function and that word is printed in the terminal. After that, an input called `guess` is created to take in the the user choice. Then, using an if statement, conditions were set to ensure the input has a length of 1 and is alphabetical.

```python
import random
word_list = ['apple', 'orange', 'lemon', 'watermelon', 'pear']
word=random.choice(word_list)
guess = input('Enter a single letter ')
if len(guess) == 1 and guess.isalpha() == True:
    print('Good guess!')
else:
    print('Oops! That is not a valid input') 
```
## Milestone 2
---
This milestone builds on the last milestone by incorporating two new functions.The first function checks that the guess is in lower case and that the letter it is in the `word` variable  . Then the second function takes the code from the previous milestone by incoparating it into a while loop which will continously run the code by setting it to `True` until the input matches the conditions which are that it needs to be one character and alphabetical. 

```python
import random
word_list = ['apple', 'orange', 'lemon', 'watermelon', 'pear']
word=random.choice(word_list)

def check_guess(guess):
    guess = guess.lower()
    if guess in word:
        print('Good guess! {} is in the word'.format(guess))
    else:
         print('Sorry, {} is not in the word. Try again'.format(guess))


def ask_for_input():
    while True:
        guess = input('Enter a single letter ')
        if len(guess) == 1 and guess.isalpha() == True:
            break
        else:
            print('Invalid letter. Please, enter a single alphabetical character.')

    check_guess(guess)

ask_for_input()
```
## Milestone 3
---
In this milestone, object-oriented programming is utilised to create the Hangman game. Firstly, a class which is the main body of the hangman code is created and the first method is the `init` method to initialise the attributes to the class. In the parameters, word list and the number of lives are defined with the `self` variable. The attributes defined in this method are the word list and the number of lives from the parameters. 

<!-- But also I initialised the word that is randomly picked by the code, the word_guessed attribute which is a list of the letters of the word with the ones not guessed replaced by '_', the number of unique letters not guessed and a list of guesses which at the start of the game is empty.   -->


```python
class Hangman:
    def __init__(self, word_list=['apple', 'orange', 'lemon', 'watermelon', 'pear'], num_lives=5):
        self.word_list = word_list 
        self.num_lives = num_lives
        self.word = random.choice(self.word_list)  # The word that is randomly picked by the code
        self.word_guessed = len(self.word)*['_'] # A list of the letters of the word with the ones not guessed replaced by '_'
        self.num_letters = len(set(self.word)) # Number of unique letter in the word
        self.list_of_guesses = [] # An empty list were guesses are appended 
```
Then the functions from the last milestone were incorporated into methods of the class. First is the `check_guess` method which now has a for-loop which if the guess is correct, replaces the `'_'` in the `word_guessed` list which the guessed letter using `enumerate`to iterate over the word to find the indexes of the guess in the word. Then by assigning the `word_guessed` to the guess, the for-loop will replace the `'_'` with the guessed letterand then outside the for-loops, `self.num_letters` is reduced by 1. Then if the guess is wrong, a statement will be printed and `self.num_lives` variable is reduced by one. Then the `ask_for_input` method is the same as the last milestone but with an elif statement which tells the user if they already inputted a letter. Finally, the instance is called with the `ask_for_input`.    
```python
    def check_guess(self,guess):
        guess = guess.lower()
        if guess in self.word:
            self.num_letters = self.num_letters - 1
            for index, char in enumerate(self.word):
                if guess in self.word:
                    if char == guess:
                        self.word_guessed[index] = guess
        else:
            self.num_lives = self.num_lives - 1
            print('Sorry, {} is not in the word'.format(guess))
            print('You have {} lives left'.format(guess))
        self.list_of_guesses.append(self.guess)
    
        print(self.word_guessed)
        print(self.num_lives)
        print(self.num_letters)       
        
                           
    def ask_for_input(self):
        while True:
            self.guess = input('Enter a single letter ')
            if len(self.guess) != 1 or self.guess.isalpha() != True:
                print('Invalid letter. Please, enter a single alphabetical character.')
            elif self.guess in self.list_of_guesses:
                print('You already tried that letter!')
                break                   
            else:
                self.check_guess(self.guess)
                self.list_of_guesses.append(self.guess)
       
                                
instance = Hangman()
instance.ask_for_input()
```
---
## Milestone 4
In the final milestone, `play_game` function was added outside of the class, which is a continuous loop that will tell the player they won if they got all the letters or that they lost if they ran out of lives by calling the Hangman class. It also calls the instance the game by calling the `ask_for_input` method. In that method,breaks were added to the elif and else statements so that the code can leave the while loop and not run an infinite loop in that method to run the rest of the loop in the `play_game` function. To run the code, the `play_game` function is called and the `word_list` was assigned as an argument.
```python
    def check_guess(self,guess):
        guess = guess.lower()
        if guess in self.word:
            self.num_letters = self.num_letters - 1
            for index, char in enumerate(self.word):
                if guess in self.word:
                    if char == guess:
                        self.word_guessed[index] = guess
        else:
            self.num_lives = self.num_lives - 1
            print('Sorry, {} is not in the word'.format(guess))
            print('You have {} lives left'.format(self.num_lives))
        self.list_of_guesses.append(self.guess)
    
        print(self.word_guessed)
     
        
                           
    def ask_for_input(self):
        while True:
            self.guess = input('Enter a single letter ')
            if len(self.guess) != 1 or self.guess.isalpha() != True:
                print('Invalid letter. Please, enter a single alphabetical character.')
            elif self.guess in self.list_of_guesses:
                print('You already tried that letter!')
                break                   
            else:
                self.check_guess(self.guess)
                self.list_of_guesses.append(self.guess)
                break


def play_game(word_list):
    game = Hangman(word_list,num_lives=5)
    while True:
        if game.num_lives == 0:
            print('You lost! The word was {}.'.format(game.word))
            break
        elif game.num_letters > 0:
            game.ask_for_input()
        elif game.num_letters <= 0 and game.num_lives > 0:
            print('Congratulations. You won the game!')
            break


play_game(word_list)

```

