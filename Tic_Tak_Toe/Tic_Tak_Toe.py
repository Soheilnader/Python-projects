# Simple X O
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

    def player(self):
        num = int(input("Your turn: "))
        while num in self.history:
            num = int(input("Type another number: "))
        self.history.append(num)
        self.frame[num - 1] = 'X'
        self.counter += 1

    def bot(self):
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

if game.check_win == 2:
    print("Draw")
x = input("Finish")
