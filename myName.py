# This program says hello and asks for my name
print('Hello world')
print('What is your name?') #ask for their name
myName = input()
print('It is good to meet you, ' + myName)
print('The length of your name is:')
print(len(myName))
print('What is your age?') #ask for their age
myAge = input()
print('You will be ' + str(int(myAge) +1) + ' in a year.')

myAge = int(myAge)
password = 'swordfish'
if myName == 'Mary':
    print('Hello Mary')
    if password == 'swordfish':
        print('Access granted.')
    else:
        print('Wrong password.')
elif myAge < 12:
    print(myAge)
elif myAge > 2000:
     print('old')

name = ''
while name != 'your name':
    print('Please type your name')
    name=input()
print('Thank you')
    
