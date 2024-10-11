

Food = {"pizza": 10, "pasta": 15, "cookies": 20}

# the "get" method returns the value of one of the keys in the dictionary
print(Food.get("pizza"))

# the "items" method takes the dictionary name and outputs the key value pairs
print(Food.items())

# the "keys" method returns the keys in the dictionary
print(Food.keys())

# the "popitem" method removes the last item in the dictionary
print(Food.popitem())
print(Food)

'''
the "setdefault" method shows what the value of a key in a dictionary is and
allows us to set a default value when a key is not in the dictionary and add that value to the dictionary
'''

print(Food.setdefault("pizza"))
print(Food)
print(Food.setdefault("cake", 30))
print(Food)

# the "update" method is used to update the dictionary with another dictionary
restaurants = {"chinese": 20, "italian": 30}
Food.update(restaurants)
print(Food)

# updating the values
restaurants = {"chinese": 15, "italian": 10}
Food.update(restaurants)
print(Food)

# adding items using the update method
Food.update(bread=20)
print(Food)
