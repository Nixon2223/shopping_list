from models.item import *

item1 = Item("tea bags", 1.50, 1, False)
item2 = Item("bread", 1.00, 1, False)
item3 = Item("bananas", 0.20, 4, False)

items = [item1, item2, item3]

def add_new_item(new_item):
    items.append(new_item)