#! /usr/bin/env python3
# Collatz sequence
print('Collatz sequence')
print('Please enter an integer :')
try :
    numb = int(input())
except ValueError:
    print('Error: Invalid argument.')
    numb=1
while numb != 1:
    #print(numb, end=' , ')
    if numb % 2 == 0:
        numb = numb // 2
    else:
        numb = numb * 3 + 1
    print(numb)
