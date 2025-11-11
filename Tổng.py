#Write a program to input size n of list a, then input n elements for list a, calculate the sum of n elements and output to the screen
n=int(input("Size: "))
l=[]
s=0
for i in range (n):
    a=float(input())
    l.append(a)
    s=s+a
print(l)
print('s =',s)