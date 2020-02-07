#hangman 1.0

import random
import os

word = ["hello"]
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

for i in range(0, len(word[0])):
    word2.append("-")
print(word2)
while wrong<=5:
    counter = 0
    print(frames[wrong])
    print("wrong letters you entered: ", wronglist)

    guess = input("one word: ")
    os.system('cls')
    if(word[0].count(guess)==0):
        wrong = wrong + 1
        wronglist.append(guess)
    else:
        for i in word[0]:
            if i == guess:
                word2[word[0].index(i)+counter]=guess
                counter=counter+1
    print(word2)
    if(word2 == list(word[0])):
        print("Done!")
        break
if(wrong==6):
    os.system('cls')
    print("You loose")
    print(frames[6])
    print("Answer was: ", list(word[0]))
input()


