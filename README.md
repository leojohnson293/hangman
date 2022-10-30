# Hangman
>Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts. This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

## Milestone 1
---
In this milestone, using python, I created a list with five different fruits. Then using the random module, I madea a variable called word that randomly chooses one of the five fruits using the choose function and prints it in the terminal. After that, I created an input that the user puts in and is printed out in the terminal. Then, using an if statement, I set conditions to ensure that the imput has a length of 1 and is alphabetical.

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
In this milestone, I built on the last one and created two new functions. The first function checks that the guess is in the word and ensures that the guess is in lower case. Then the second function bulids on the code from the first milestone by incoparating it into a while loop which will continously run the code by setting it to True until the input matches the conditions which are that it needs to be one character and alphabetical. 

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
In this milestone,
```python
import random

class Hangman:
    def __init__(self, word_list=['apple', 'orange', 'lemon', 'watermelon', 'pear'], num_lives=5):
        self.word_list = word_list 
        self.num_lives = num_lives
        self.word = random.choice(self.word_list)  
        self.word_guessed = len(self.word)*['_']
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

    def check_guess(self,guess):
        guess = guess.lower()
        if guess in self.word:
            self.num_letters = self.num_letters - 1
            for i in self.word:
                i = self.word.find(guess)
                self.word_guessed[i] = guess
            for j in self.word:
                j = self.word.rfind(guess)
                self.word_guessed[j] = guess
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



