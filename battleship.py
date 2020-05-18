from random import randint
s='yes'
while s=='yes':
    L=[10000]
    for i in range(0,4):
        for j in range(0,4):
            L[i][j]=randint(0,2)
    m=eval(input('enter row number'))
    n=eval(input('enter column number'))
    if L[m][n]==1:
        print('Hit')
    elif L[m][n]==0:
        print('Miss')
    s=input('do you want to continue? answer yes or no')
     
