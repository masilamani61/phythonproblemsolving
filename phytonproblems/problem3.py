def series(a):
    if a%2==0:
        a=a-1
    c=1
    for i in range(a):
        print(c,end=',')
        c=c+2
a=int(input())
series(a)
    
