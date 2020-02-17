import os, re

myFile = open('hellorep.txt','w')
myFile.write('The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was ADERB unaffected by these events.')
myFile.close()

myFile = open('hellorep.txt')
content = myFile.read()
print(content)
print('Enter an adjective:')
myAdj = input()
print('Enter a noun:')
myNoun = input()
print('Enter a verb:')
myVerb = input()
print('Enter a adverb:')
myAdverb = input()
# print(myAdj + ' ' + myNoun + ' ' + myVerb + ' ' + myAdverb)
adjRegex = re.compile('ADJECTIVE')
nounRegex = re.compile('NOUN')
verbRegex = re.compile('VERB')
adverbRegex = re.compile('ADERB')
content = adjRegex.sub(myAdj,content)
content = nounRegex.sub(myNoun,content)
content = verbRegex.sub(myVerb,content)
content = adverbRegex.sub(myAdverb,content)
print(content)
outFile = open('helloOut.txt','w')
outFile.write(content)
outFile.close()