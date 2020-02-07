#hangman 1.0

import random
import os

word = ["hello","apple","country","football","avenger","development"]
word2 = []
wrong = 0
frames = ["""
 +---+
  |   |
      |
      |
      |
      |
=========
""","""
  +---+
  |   |
  O   |
      |
      |
      |
=========
""","""
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
""","""
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
""","""
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
""","""
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
""","""
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
"""]
wronglist = []
counter = 0
rnd = random.randrange(0,len(word))
def winscreen():
    print("""
    |@@@@|     |####|
    |@@@@|     |####|
    |@@@@|     |####|
    \@@@@|     |####/
     \@@@|     |###/
      `@@|_____|##'
           (O)
        .-'''''-.
      .'  * * *  `.
     :  *       *  :
    :  W I N N E R  :
    : ~           ~ :
     :  *       *  :
      `.  * * *  .'
        `-.....-'""")


for i in range(0, len(word[rnd])):
    word2.append("-")
print(word2)
while wrong<=5:
    counter = 0
    print(frames[wrong])
    print("wrong letters you entered: ", wronglist)

    guess = input("one letter: ")
    os.system('cls')
    if(word[rnd].count(guess)==0):
        wrong = wrong + 1
        wronglist.append(guess)
    else:
        for i in range(len(word[rnd])):
            if word[rnd][i] == guess:
                word2[i]=guess

    print(word2)
    if(word2 == list(word[rnd])):
        print("You Won!")
        winscreen()
        break
if(wrong==6):
    os.system('cls')
    print("Looser :)")
    print(frames[6])
    print("Answer was: ", list(word[rnd]))
input()


