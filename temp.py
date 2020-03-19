a=1;b=1
n=int(input('enter the number of fibonacci numbers required'))
print(a,',',b,end=',')
for i in range(2,n):
    c=a+b
    a=b
    b=c
    print(c,end=',')
   
