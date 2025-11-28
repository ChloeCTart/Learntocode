<<<<<<< HEAD
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
=======
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
>>>>>>> 6e59fb38dec1ac65d00793cd7898b1317dd93d49
    print(c)