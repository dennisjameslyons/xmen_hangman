import random
import time
import sys

def hangman():

    word = random.choice(["ProfessorX","JeanGrey", "Rogue", "Wolverine", "Cyclops", "Beast", "Morph", "Jubilee", "Gambit", "Magneto" ])
    validLetters = "abcdefghijklmnopqrstuvwxyz"
    turns = 5
    guessmade = ""
    start_time = time.time()

    def slowprint(s):
        for c in s + '\n':
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(1./5)

    while len(word) > 0:
        main = ""
        missed = 0

        for letter in word:
            if letter in guessmade:
                main = main + letter
            else:
                main = main + "_" + " "

        if main == word:
            print(main)
            print("Congratulations! ")
            break

        print("Guess a letter: ", main)
        guess = input()

        if guess == word[0].lower():
            guessmade = guessmade + guess.upper()

        if guess in validLetters:
            guessmade = guessmade + guess
        elif guess == word:
            print(main)
            print("Congradulations! You guessed the word!")
            break
        else:
            print("Enter a valid entry, a-z only please. ")
            guess = input()

        if guess not in word.lower():
            turns = turns -1
            if turns < 2 and turns > 0:
                print(("You have ")+(str(turns))+(" turns left. "))
                print("_ - _ - _ - ")
            elif turns < 1:
                print("So sorry, you have lost. \nF\nrO\nwNiE\n F\naC\ne :P")
                break


name = input("Enter your name please: ")
print("Welcome,", name)
hangman()
