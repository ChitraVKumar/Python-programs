inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']


def displayInventory(stuff):
    bag = 0
    for key, value in stuff.items():
        print(str(value) + ' ' + key)
        bag += value
    print("Total items in bag: ", bag)


displayInventory(inventory)
