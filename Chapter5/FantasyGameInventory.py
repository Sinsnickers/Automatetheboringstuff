#Fanatasy Game Inventory

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
inv = {"gold_coin" : 42, "rope" : 1}
dragonLoot = ["gold_coin" , "dagger" ,"gold_coin" , "gold_coin" , "ruby"]


def displayInventory(inventory):
    print("Inventory:")
    item_total=0
    for key , value in inventory.items():
        print(value, key)
        item_total+=value
    print("Total number of items: " + str(item_total))

def addToInventory(inventory,loot):
    for item in loot:
        inventory.setdefault(item,0)
        inventory[item] += 1



#displayInventory(stuff)
displayInventory(inv)
addToInventory(inv,dragonLoot)
displayInventory(inv)