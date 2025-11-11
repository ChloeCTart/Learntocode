#Write a program that allows input of a positive integer N and checks whether N is a prime number or not.
n=int(input('n = '))
u=0
for i in range (2,n):
    if n%i==0:
        u=u+1
if u==0:
    if n==0 or n==1:
        print(n, 'không là số nguyên tố')
    else:
        print(n, 'là số nguyên tố')
else:
    print(n, 'không là số nguyên tố')
    print('u = ',u)