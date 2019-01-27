print('Hello world')
print('What is your name?')

myName = input()
print(myName)
print('It is good to meet you, '+ myName)
print('The length of your name is: ')
print(len(myName))
print('What is your age?')
myAge = input()
print('You will be ' +str(int(myAge) +1) + ' in a year.')
print('Please enter password :')
password = input()
if myName == 'Daniel':
    print('Hello Daniel')
    if password == 'swordfish':
        print('Access granted')
    else:
        print('Wrong password')
spam = 0
while spam < 5:
    print('Hello, World')
    spam += 1
