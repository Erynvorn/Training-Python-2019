def spam():
    eggs = 'spam local'
    print(eggs)

def bacon():
    eggs = 'bacon local'
    print(eggs)
    spam()
    print(eggs)

eggs = 'Global'
bacon()
print(eggs)

def pommes():
    global apple
    apple = 'pommes'

apple = 'global'
pommes()
print(apple)

