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