#Write a program that allows the input of a positive integer N, creating a right-angled triangle with the sign *, the right-angled sides have N signs *
n=int(input('Độ dài cạnh: '))
for i in range (1, n+1):
    print(i*'* ')