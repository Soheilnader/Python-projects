# Simple X O
# Version: 2
# By: Soheil

import random
import os

class Game:
    frame = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    history = []
    counter = 0

    def show_frame(self):
        os.system('cls')
        for i in range(9):
            print(self.frame[i], end = ' ')
            if i == 2 or i == 5 or i == 8:
                print()
        #print("frame: ", self.frame)
        #print("history: ", self.history)
        #print("counter: ", self.counter)

    def player(self):
        num = int(input("Your turn: "))
        while num in self.history:
            num = int(input("Type another number: "))
        self.history.append(num)
        self.frame[num - 1] = 'X'
        self.counter += 1

    def bot(self):
        #Attack
        #Row 1:
        if (self.frame[0] == 'O' and self.frame[1] == 'O') and (self.frame[2] == 3):
            self.frame[2] = 'O'
            self.history.append(2 + 1)
            self.counter += 1
        elif (self.frame[0] == 'O' and self.frame[2] == 'O') and (self.frame[1] == 2):
            self.frame[1] = 'O' 
            self.history.append(1 + 1)
            self.counter += 1
        elif (self.frame[1] == 'O' and self.frame[2] == 'O') and (self.frame[0] == 1):
            self.frame[0] = 'O' 
            self.history.append(0 + 1)
            self.counter += 1
        #Row 2:
        elif (self.frame[3] == 'O' and self.frame[4] == 'O') and (self.frame[5] == 6):
            self.frame[5] = 'O' 
            self.history.append(5 + 1)
            self.counter += 1
        elif (self.frame[3] == 'O' and self.frame[5] == 'O') and (self.frame[4] == 5):
            self.frame[4] = 'O' 
            self.history.append(4 + 1)
            self.counter += 1
        elif (self.frame[4] == 'O' and self.frame[5] == 'O') and (self.frame[3] == 4):
            self.frame[3] = 'O' 
            self.history.append(3 + 1)
            self.counter += 1
        #Row 3:
        elif (self.frame[6] == 'O' and self.frame[7] == 'O') and (self.frame[8] == 9):
            self.frame[8] = 'O' 
            self.history.append(8 + 1)
            self.counter += 1
        elif (self.frame[6] == 'O' and self.frame[8] == 'O') and (self.frame[7] == 8):
            self.frame[7] = 'O' 
            self.history.append(7 + 1)
            self.counter += 1
        elif (self.frame[7] == 'O' and self.frame[8] == 'O') and (self.frame[6] == 7):
            self.frame[6] = 'O' 
            self.history.append(6 + 1)
            self.counter += 1
        #Column 1:
        elif (self.frame[0] == 'O' and self.frame[3] == 'O') and (self.frame[6] == 7):
            self.frame[6] = 'O' 
            self.history.append(6 + 1)
            self.counter += 1
        elif (self.frame[0] == 'O' and self.frame[6] == 'O') and (self.frame[3] == 4):
            self.frame[1] = 'O' 
            self.history.append(3 + 1)
            self.counter += 1
        elif (self.frame[3] == 'O' and self.frame[6] == 'O') and (self.frame[0] == 1):
            self.frame[0] = 'O' 
            self.history.append(0 + 1)
            self.counter += 1
        #Column 2:
        elif (self.frame[1] == 'O' and self.frame[4] == 'O') and (self.frame[7] == 8):
            self.frame[7] = 'O' 
            self.history.append(7 + 1)
            self.counter += 1
        elif (self.frame[1] == 'O' and self.frame[7] == 'O') and (self.frame[4] == 5):
            self.frame[4] = 'O' 
            self.history.append(4 + 1)
            self.counter += 1
        elif (self.frame[4] == 'O' and self.frame[7] == 'O') and (self.frame[1] == 2):
            self.frame[1] = 'O' 
            self.history.append(1 + 1)
            self.counter += 1
        #Column 3:
        elif (self.frame[2] == 'O' and self.frame[5] == 'O') and (self.frame[8] == 9):
            self.frame[8] = 'O' 
            self.history.append(8 + 1)
            self.counter += 1
        elif (self.frame[2] == 'O' and self.frame[8] == 'O') and (self.frame[5] == 6):
            self.frame[5] = 'O' 
            self.history.append(5 + 1)
            self.counter += 1
        elif (self.frame[5] == 'O' and self.frame[8] == 'O') and (self.frame[2] == 3):
            self.frame[2] = 'O' 
            self.history.append(2 + 1)
            self.counter += 1
        #Cross 1:
        elif (self.frame[0] == 'O' and self.frame[4] == 'O') and (self.frame[8] == 9):
            self.frame[8] = 'O' 
            self.history.append(8 + 1)
            self.counter += 1
        elif (self.frame[0] == 'O' and self.frame[8] == 'O') and (self.frame[4] == 5):
            self.frame[4] = 'O' 
            self.history.append(4 + 1)
            self.counter += 1
        elif (self.frame[4] == 'O' and self.frame[8] == 'O') and (self.frame[0] == 1):
            self.frame[0] = 'O' 
            self.history.append(0 + 1)
            self.counter += 1
         #Cross 2:
        elif (self.frame[2] == 'O' and self.frame[4] == 'O') and (self.frame[6] == 7):
            self.frame[6] = 'O' 
            self.history.append(6 + 1)
            self.counter += 1
        elif (self.frame[2] == 'O' and self.frame[6] == 'O') and (self.frame[4] == 8):
            self.frame[4] = 'O' 
            self.history.append(4 + 1)
            self.counter += 1
        elif (self.frame[4] == 'O' and self.frame[6] == 'O') and (self.frame[2] == 3):
            self.frame[2] = 'O' 
            self.history.append(2 + 1)
            self.counter += 1

        #Defence
        #Row 1:
        elif (self.frame[0] == 'X' and self.frame[1] == 'X') and (self.frame[2] == 3):
            self.frame[2] = 'O'
            self.history.append(2 + 1)
            self.counter += 1
        elif (self.frame[0] == 'X' and self.frame[2] == 'X') and (self.frame[1] == 2):
            self.frame[1] = 'O' 
            self.history.append(1 + 1)
            self.counter += 1
        elif (self.frame[1] == 'X' and self.frame[2] == 'X') and (self.frame[0] == 1):
            self.frame[0] = 'O' 
            self.history.append(0 + 1)
            self.counter += 1
        #Row 2:
        elif (self.frame[3] == 'X' and self.frame[4] == 'X') and (self.frame[5] == 6):
            self.frame[5] = 'O' 
            self.history.append(5 + 1)
            self.counter += 1
        elif (self.frame[3] == 'X' and self.frame[5] == 'X') and (self.frame[4] == 5):
            self.frame[4] = 'O' 
            self.history.append(4 + 1)
            self.counter += 1
        elif (self.frame[4] == 'X' and self.frame[5] == 'X') and (self.frame[3] == 4):
            self.frame[3] = 'O' 
            self.history.append(3 + 1)
            self.counter += 1
        #Row 3:
        elif (self.frame[6] == 'X' and self.frame[7] == 'X') and (self.frame[8] == 9):
            self.frame[8] = 'O' 
            self.history.append(8 + 1)
            self.counter += 1
        elif (self.frame[6] == 'X' and self.frame[8] == 'X') and (self.frame[7] == 8):
            self.frame[7] = 'O' 
            self.history.append(7 + 1)
            self.counter += 1
        elif (self.frame[7] == 'X' and self.frame[8] == 'X') and (self.frame[6] == 7):
            self.frame[6] = 'O' 
            self.history.append(6 + 1)
            self.counter += 1
        #Column 1:
        elif (self.frame[0] == 'X' and self.frame[3] == 'X') and (self.frame[6] == 7):
            self.frame[6] = 'O' 
            self.history.append(6 + 1)
            self.counter += 1
        elif (self.frame[0] == 'X' and self.frame[6] == 'X') and (self.frame[3] == 4):
            self.frame[1] = 'O' 
            self.history.append(3 + 1)
            self.counter += 1
        elif (self.frame[3] == 'X' and self.frame[6] == 'X') and (self.frame[0] == 1):
            self.frame[0] = 'O' 
            self.history.append(0 + 1)
            self.counter += 1
        #Column 2:
        elif (self.frame[1] == 'X' and self.frame[4] == 'X') and (self.frame[7] == 8):
            self.frame[7] = 'O' 
            self.history.append(7 + 1)
            self.counter += 1
        elif (self.frame[1] == 'X' and self.frame[7] == 'X') and (self.frame[4] == 5):
            self.frame[4] = 'O' 
            self.history.append(4 + 1)
            self.counter += 1
        elif (self.frame[4] == 'X' and self.frame[7] == 'X') and (self.frame[1] == 2):
            self.frame[1] = 'O' 
            self.history.append(1 + 1)
            self.counter += 1
        #Column 3:
        elif (self.frame[2] == 'X' and self.frame[5] == 'X') and (self.frame[8] == 9):
            self.frame[8] = 'O' 
            self.history.append(8 + 1)
            self.counter += 1
        elif (self.frame[2] == 'X' and self.frame[8] == 'X') and (self.frame[5] == 6):
            self.frame[5] = 'O' 
            self.history.append(5 + 1)
            self.counter += 1
        elif (self.frame[5] == 'X' and self.frame[8] == 'X') and (self.frame[2] == 3):
            self.frame[2] = 'O' 
            self.history.append(2 + 1)
            self.counter += 1
        #Cross 1:
        elif (self.frame[0] == 'X' and self.frame[4] == 'X') and (self.frame[8] == 9):
            self.frame[8] = 'O' 
            self.history.append(8 + 1)
            self.counter += 1
        elif (self.frame[0] == 'X' and self.frame[8] == 'X') and (self.frame[4] == 5):
            self.frame[4] = 'O' 
            self.history.append(4 + 1)
            self.counter += 1
        elif (self.frame[4] == 'X' and self.frame[8] == 'X') and (self.frame[0] == 1):
            self.frame[0] = 'O' 
            self.history.append(0 + 1)
            self.counter += 1
         #Cross 2:
        elif (self.frame[2] == 'X' and self.frame[4] == 'X') and (self.frame[6] == 7):
            self.frame[6] = 'O' 
            self.history.append(6 + 1)
            self.counter += 1
        elif (self.frame[2] == 'X' and self.frame[6] == 'X') and (self.frame[4] == 8):
            self.frame[4] = 'O' 
            self.history.append(4 + 1)
            self.counter += 1
        elif (self.frame[4] == 'X' and self.frame[6] == 'X') and (self.frame[2] == 3):
            self.frame[2] = 'O' 
            self.history.append(2 + 1)
            self.counter += 1

        #Random
        else:
            if self.counter != 9:
                num = random.randrange(1,10)
                while num in self.history:
                    num = random.randrange(1,10)
                self.history.append(num)
                self.frame[num - 1] = 'O'
                self.counter += 1

    def check_win(self):
        #Player wins:
        if self.frame[0] == self.frame[1] == self.frame[2] == 'X':
            return 1
        if self.frame[3] == self.frame[4] == self.frame[5] == 'X':
            return 1
        if self.frame[6] == self.frame[7] == self.frame[8] == 'X':
            return 1
        if self.frame[0] == self.frame[3] == self.frame[6] == 'X':
            return 1
        if self.frame[1] == self.frame[4] == self.frame[7] == 'X':
            return 1
        if self.frame[2] == self.frame[5] == self.frame[8] == 'X':
            return 1
        if self.frame[0] == self.frame[4] == self.frame[8] == 'X':
            return 1
        if self.frame[2] == self.frame[4] == self.frame[6] == 'X':
            return 1

        #bot wins
        if self.frame[0] == self.frame[1] == self.frame[2] == 'O':
            return 0
        if self.frame[3] == self.frame[4] == self.frame[5] == 'O':
            return 0
        if self.frame[6] == self.frame[7] == self.frame[8] == 'O':
            return 0
        if self.frame[0] == self.frame[3] == self.frame[6] == 'O':
            return 0
        if self.frame[1] == self.frame[4] == self.frame[7] == 'O':
            return 0
        if self.frame[2] == self.frame[5] == self.frame[8] == 'O':
            return 0
        if self.frame[0] == self.frame[4] == self.frame[8] == 'O':
            return 0
        if self.frame[2] == self.frame[4] == self.frame[6] == 'O':
            return 0

        #Draw
        else:
            return 2
        

game = Game()

while game.counter != 9:
    game.show_frame()
    game.player()
    game.show_frame()
    if game.check_win() == 1:
        print("Player won")
        break
    game.bot()
    game.show_frame()
    if game.check_win() == 0:
        print("bot won")
        break

if game.check_win() == 2:
    print("Draw")
x = input("Finish")
