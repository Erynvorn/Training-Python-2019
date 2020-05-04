import os


myPath = '/Users/danielseite/Documents/Training-Python-2019'
print(os.getcwd())
print(myPath)


helloFile = open('hello.txt','w')
for file in os.listdir('.'):
    helloFile.write(file)
    helloFile.write(' '+str(os.path.getsize(os.path.join(myPath,file))))
    helloFile.write('\n')
helloFile.close()
helloFile = open('hello.txt')
content = helloFile.read()
helloFile.close()
print(content)

