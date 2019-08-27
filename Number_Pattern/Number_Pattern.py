#By: Soheil
a1=int(input())
a2=int(input())
a3=int(input())
a4=int(input())

d1=a2-a1
d2=a3-a2
d3=a4-a3

q1=a2/a1
q2=a3/a2
q3=a4/a3

if d1==d2==d3 :
	print(d1,'n+',a1-d1,sep='')

elif q1==q2==q3 :
	print(a1,'*',q1,'^(n-1)',sep='')

else :
	print("Error!")
