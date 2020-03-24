a=int(input('enter any number between 1 and 9'))
from random import randint
x=randint(1,10)
if x==a:
    print('CONGRATS!!, YOU WON!!')
else:
    print('THE NUMBER IS:',x,'BETTER LUCK NEXT TIME.')
