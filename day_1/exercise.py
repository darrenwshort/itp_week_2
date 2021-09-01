# ITP Week 2 Day 1 Exercise


# Dictionary Loop

inventory = {
    "soda_cans": 45,
    "chips": 12,
    "sandwiches": 34,
    "candy": 1
}

#print out original dictionary before we modify it.
print()
print("original dictionary:")
print("\t", inventory)
print()


# SCENARIO: A person came in and bought one of everything!

#loop through dictionary and increment count of each item by 1.
for item in inventory.items():
    # decrement item by using an assignment operator (Day 2 Lecture line #130)
    inventory.update({item[0]: item[1] + 1})
    # NOTE: recall that item represents the key of the key:value pair


#print dictionary after running increment to values. 
#all item values should be increased by 1.
print("dictionary after item values have been incremented by 1:")
print("\t", inventory) 
print()



# SCENARIO: REMOVE ANY 0 ITEMS

#adding some "zero" items for removal (plus some others)
inventory["slushee"] = 0
inventory["hotdogs"] = 3
inventory["donuts"] = 0
inventory["nachos"] = 8

#print current dictionary
print("\ndictionary with extra items added:")
print("\t", inventory)
print()


del_list = []   #create empty list
for item in inventory.items():
    # use an if statement to check if the value is 0 and then remove it
    if(item[1] == 0):
        del_list.append(item[0])  #build list of keys that need to be deleted

for k in del_list:        #loop through list of items to be deleted, by key
    del inventory[k]      #delete item based on current k

print("dictionary after *zero* items have been removed.")
print("\t", inventory)          #print inventory to show if any items where deleted.
print()
