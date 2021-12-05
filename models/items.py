from models.item import *

item1 = Item("tea bags", 1.50, 1, False)
item2 = Item("bread", 1.00, 1, False)
item3 = Item("bananas", 0.20, 4, True)
item4 = Item("tea bags", 1.50, 1, False)
item5 = Item("bread", 1.00, 1, False)
item6 = Item("bananas", 0.20, 4, False)
item7 = Item("tea bags", 1.50, 1, False)
item8 = Item("bread", 1.00, 1, True)
item9 = Item("bananas", 0.20, 4, False)

items = [item1, item2, item3, item4, item5, item6, item7, item8, item9]

def add_new_item(new_item):
    items.append(new_item)

def total_price(items):
    total_price = 0
    for item in items:
          total_price += float(item.price) * float(item.quantity)
    return "%.2f" % float(total_price)

def filter_bought(items, i):
    new_list = []
    if i == "T":
        for item in items:
            if item.bought == True:
                new_list.append(item)
    if i == "A":
        for item in items:
                new_list.append(item)
    if i == "F":
        for item in items:
            if item.bought == False:
                new_list.append(item)
    return new_list
      

