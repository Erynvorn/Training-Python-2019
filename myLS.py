import os
for fileName in os.listdir():
    print(fileName)
pat = os.path.abspath('.')
pat2 = os.path.abspath('..')
print(pat)
print(pat2)
print(os.path.abspath('.'))
print(os.getcwd())
#for fileName in os.listdir():
#   print(fileName)
    
