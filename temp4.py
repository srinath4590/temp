arr=array.array(i)
for i in range(0,10):
    arr[i]=int(input())
    for j in range(0,n-i-1):
        if a[j]>a[j+1]:
            t=a[j]
            a[j]=a[j+1]
            a[j+1]=t
for i in range(0,n):
    if a[i+1]<a[i]:
        s=a[i+1]
        break
print('second largest mark',s)
