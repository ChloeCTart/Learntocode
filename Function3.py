def d_to_b(d):
    b=0
    thuong=d
    hang=0
    while thuong!=0:
        if thuong%2==0:
            x=0*(10**hang)
        if thuong%2==1:
            x=1*(10**hang)
        b=b+x
        hang=hang+1
        thuong=thuong//2
    print('Nhi phan: ',b)
d=int(input('Thap phan: '))
d_to_b(d)