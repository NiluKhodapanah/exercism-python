def create_inventory(inp):
    inventory = {}
    for i in inp:
        inventory[i] = inventory.get(i, 0) + 1
    return inventory

def add_items(inventory, it_list):
    for item in it_list:
        inventory[item] = inventory.get(item, 0) + 1
    return inventory

def decrement_items(inventory, item_list):
    for item in item_list:
        if item in inventory and inventory[item] > 0:
            inventory[item] -= 1
    return inventory

def remove_item(inventory, item):
    if item in inventory:
        del inventory[item]
    return inventory

def list_inventory(inventory):
    result = []
    for k, v in inventory.items():
        if v > 0:
            result.append((k, v))  # Add only items with v > 0
    return result
        