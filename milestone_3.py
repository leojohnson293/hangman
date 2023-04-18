import random

class Hangman:
    def __init__(self, word_list=['apple', 'orange', 'lemon', 'watermelon', 'pear',], num_lives=5):
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

