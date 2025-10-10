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
    for line in hangman_art[wrong_guesses]:
        print(line)

def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print(" ".join(answer))

def main():
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guessed_letters = set()
    is_running = True

    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)
        # display_answer(answer)
        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid inpput")
            continue
        if guess in guessed_letters:
            print(f"{guess} is already guessed")
            continue

        guessed_letters.add(guess)

        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] == guess
        else:
            wrong_guesses += 1

        if "_" not in hint:
            display_man(wrong_guesses)
            display_answer(answer)
            print("YOU WIN!")
            is_running = False
        elif wrong_guesses >= len(hangman_art) - 1:
            display_hint(wrong_guesses)
            display_answer(answer)
            print("YOU LOSE!")
            is_running = False

if __name__ == '__main__':
    main()