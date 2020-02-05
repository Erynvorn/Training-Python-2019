import os

myPath = os.path.abspath('.')

print(os.path.abspath(myPath))
print(os.path.isabs(myPath))
print(os.path.relpath(myPath,'/Users'))
# print(os.path.abspath(os.path.relpath(myPath,'/Users')))
print(os.getcwd())

print(os.path.dirname(myPath))
print(os.path.basename(myPath))
print(os.path.split(myPath))

# os.makedirs(os.path.join(myPath, 'myTestFolder3'))
os.chdir(os.path.join(myPath, 'myTestFolder'))
print(os.getcwd())

myPath2 = os.path.abspath('..')
print(os.getcwd())
print(myPath2)


helloFile = open('hello.txt','w')
helloFile.write('Hello world!\n')
helloFile.close()
print(os.path.abspath('hello.txt'))
helloFile = open('hello.txt','a')
helloFile.write('Bacon is not a vegetable')
helloFile.close()
helloFile = open('hello.txt')
contnet = helloFile.read()
helloFile.close()
print(contnet)
helloFile= open('hello.txt','a')
for file in os.listdir('..'):
    helloFile.write(file)
    helloFile.write('\n')
helloFile.close()
helloFile = open('hello.txt')
contnet = helloFile.read()
helloFile.close()
print(contnet)

