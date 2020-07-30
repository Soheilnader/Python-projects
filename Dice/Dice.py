#By: Soheil
import random
y=True
while(y):
    x = input("Press enter to roll dice, if you wanna quit, type \"quit\": ")
    rnd = random.choice(range(1,7))
    if x == 'quit':
        y=False
    else:
        print(rnd)
        if rnd == 6:
            print("""
#########
# 0   0 #
# 0   0 #
# 0   0 #
#########""")

        if rnd == 5:
            print("""
#########
# 0   0 #
#   0   #
# 0   0 #
#########""")
        if rnd == 4:
            print("""
#########
# 0   0 #
#       #
# 0   0 #
#########""")

        if rnd == 3:
            print("""
#########
#     0 #
#   0   #
# 0     #
#########""")

        if rnd == 2:
            print("""
#########
#     0 #
#       #
# 0     #
#########""")

        if rnd == 1:
            print("""
#########
#       #
#   0   #
#       #
#########""")
