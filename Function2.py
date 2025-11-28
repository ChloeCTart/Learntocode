def gcd(a,b):
    if a==0 or b==0:
        gcd=0
    elif a>b:
        for i in range(1,a+1):
            if a%i==0 and b%i==0:
                gcd=i
    elif a<b:
        for i in range(1,b+1):
            if a%i==0 and b%i==0:
                gcd=i
    else:
        gcd=a
    print('Uoc chung lon nhat cua',a,'va',b,'la',gcd)
def lcm(a,b):
    x=0
    if a==0 or b==0:
        lcm=0
    else:
        lcm=0
        while x==0:
            lcm=lcm+1
            if lcm%a==0 and lcm%b==0:
                x=x+1
    print('Boi chung nho nhat cua',a,'va',b,'la',lcm)
a=int(input('a = '))
b=int(input('b = '))
gcd(a,b)
lcm(a,b)