# By: Soheil
num = int(input("enter a num: "))
x = range(0,num)
z = 1
y = range(0,z)
for n in x:
    for p in y:
        z += 1
        y = range(0, z)
        print("*", end='')
    print()
    z = 1