def calculator(a,b,c):
    
    if c=='+':
        return a+b

    elif c=='-':
        return a-b


    elif c=='X':
        return a*b

    elif c=='/':
        return a/b
a=int(input())
b=int(input())
c=input()
print(calculator(a,b,c))
