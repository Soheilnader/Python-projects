#By: Soheil
import random
dice=['ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX']
y=True
while(y):
    x = input("Press enter to roll dice, if you wanna quit, type \"quit\": ")
    if x == 'quit':
        y=False
    else:
        print(random.choice(dice))

