def getdict(listelement):
    a={}
    for i in [1,2,3,4,5,6,7,8,9]:
        count=0
        for j in listelement:
            if j%i==0:
                count=count+1
        a[i]=count
    return a
listelemt_len=int(input())
listelement=[]
for i in range(listelemt_len):
    element=int(input())
    listelement.append(element)
print(getdict(listelement))
