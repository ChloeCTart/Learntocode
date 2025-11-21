#Write a program to input n and print out the nth Fibonacci number
n=int(input('Số thứ: '))
a=1
b=1
c=0
if n==1 or n==2:
    print('1')
else:
    for i in range(1,n-1):
        c=a+b
        a=b
        b=c
    print(c)