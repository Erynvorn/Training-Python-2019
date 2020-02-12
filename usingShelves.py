import shelve
shelfFile = shelve.open('mydataShelved')
cats = ['Sophie', 'Pooka', 'Simon']
shelfFile['cats'] = cats
shelfFile.close()
shelfFile = shelve.open('mydataShelved')
print(type(shelfFile))
print(shelfFile['cats'])
print(list(shelfFile.keys()))
print(list(shelfFile.values()))
shelfFile.close()
