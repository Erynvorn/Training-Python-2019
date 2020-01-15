gamerOne = {'rope':1,'torch':6, 'gold coin':42, 'dagger':1, 'arrow':12}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
def displayInventory(gamer):
    total = 0
    print('Inventory')
    for k,v in gamer.items():
        print(str(v)+ '  '+k)
        total += v
    print('Total number of item: '+str(total))

def addToInventory(inventory,addedItems):
    for i in addedItems:
        inventory.setdefault(i,0)
        inventory[i] += 1
    return inventory

displayInventory(gamerOne)
gamerOne = addToInventory(gamerOne, dragonLoot)
displayInventory(gamerOne)
#print(gamerOne)
