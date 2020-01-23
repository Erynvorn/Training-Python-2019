# Collatz sequence
def collatz(number):
    if number % 2 == 0:
        return number/2
    else:
        return number *3 + 1
    
while True:
    print('Enter number:')
    try :
        start = int(input())
    except ValueError:
        print('Please enter an integer')
        continue

    while start != 1:
        start = collatz(start)
        print(str(int(start)))
    #print('1')
        
