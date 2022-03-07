def displayInventory(stuff):
    bag = 0
    for key, value in stuff.items():
        print(str(value) + ' = ' + key)
        bag += value
    print("Total items in bag = ", bag)


def addInventory(inventory, addedItems):
    for i in addedItems:
        inventory.setdefault(i, 0)  # This adds the key to the dictionary, if not found adds and sets the value to zero
        inventory[i] += 1
    return inventory


inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby', 'potion']
inventory = addInventory(inventory, dragonLoot)
displayInventory(inventory)
