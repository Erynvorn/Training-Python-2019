name=''
while not name:
    print('Enter your name:')
    name = input()
print('How many guests will you have ' + name +' ?')
numOfGuests = int(input())
if numOfGuests:
    print('Wow, ' + str(numOfGuests)+ ' guests !')
print('Done')
