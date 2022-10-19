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

