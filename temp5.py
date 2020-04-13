L=[]
n=int(input('enter the number of entries'))
for i in range(0,n):
    n=eval(input('enter marks'))
    L.append(n)
    L.sort()
    L.reverse()
for j in range(0,n):
    if L[j]<L[j-1]:
        print(L[j])
        break
