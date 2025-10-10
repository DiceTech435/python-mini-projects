# Hangman Game in Python
import random

words = ("apple", "orange", "banana", "cocunut", "pineapple")

# Dictionary of key:()
hangman_art = {0: ("   ",
                   "   ",
                   "   "), 
               1: (" º ",
                   "   ",
                   "   "), 
               2: (" º ",
                   " | ",
                   "   "), 
               3: (" º ",
                   "/| ",
                   "   "), 
               4: (" º ",
                   "/|\\",
                   "   "), 
               5: (" º  ",
                   "/|\\ ",
                   "/  "), 
               6: (" º ",
                   "/|\\",
                   "/ \\")}

# for line in hangman_art[6]:
#     print(line)

def display_man(wrong_guesses):
    pass

def display_yint(hint):
    pass

def display_answer(answer):
    pass

def main():
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guessed_letters = set()


if __name__ == '__main__':
    main()