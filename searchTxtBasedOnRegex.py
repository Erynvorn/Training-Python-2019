import os, re


myPath = '/Users/danielseite/Documents/Training-Python-2019'
print(os.getcwd())
print(myPath)

print('Insert your Regex')
myRegexInput = input()

myRegex = re.compile(myRegexInput)

myTextRegex = re.compile(r'.txt$')

for file in os.listdir('.'):
    if os.path.isfile(file):
        if myTextRegex.search(file) != None:
            helloFile = open(file)
            helloContent = helloFile.read()
            if myRegex.search(helloContent) != None:
                print(file+ ' is a match')
 
        



