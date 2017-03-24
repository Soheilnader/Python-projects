#By: Soheil Nadernezhad

x1=int(input("Enter 4 numbers:"))
x2=int(input())
x3=int(input())
x4=int(input())

y1=x2-x1
y2=x3-x2
y3=x4-x3

if y3==y2==y1 :
    a=0
    if y1>x1+a :
        while y1 >= x1+a:
            a += 1
            if y1==x1+a:
               print(y1,"n-",a)
               break
    if y1<x1+a :
        while y1 <= x1+a:
            a -= 1
            if y1==x1+a:
               print(y1,"n+",abs(a))
               break
    if y1==x1:
        print (y1,'n')
else:
    print("error!")

input()
