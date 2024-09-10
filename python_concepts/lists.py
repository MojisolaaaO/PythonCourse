"""
Lists are a collection of data
Lists can contain any/all data types in a single list
Lists can contain other collections (lists, dictionaries, tuples) as list items
Lists are mutable (items can be added, removed, changed)
Lists maintain order (an index can be used find an index)

"""

fruits = ["apples", "pears", "grapes"]
years = [3, "2000", 4.5, 900, "2024"]

print(fruits, years)

# "append" adds an item to a list
fruits.append("pineapple")
print(fruits)

# "extend" allows to extend the list with another list
fruits.extend(years)
# this would print the fruits and years list into one list
print(fruits)


# remove an items from a list
fruits.remove("apples")
print(fruits)

# removing an item by index
# to remove the first item, use the "pop" method
fruits.pop(0)
print(fruits)

# to remove the last item but do not know the length of thr list, use negative indexing
fruits.pop(-1)
print(fruits)

# to sort numbers in ascending order, use the "sort" method
numbers = [20, 24, 28, 26, 22, 30, 22.5, 28.8]
numbers.sort()
print(numbers)

# the "in" function allows us to check membership in a list. The result is either True or FaLse
print("grapes" in fruits)

# the "count" function allows us to check membership and number of items in the list
print(fruits.count("grapes"))


# the "index" function allows us to check the membership and index of an item in a list
print(fruits.index("pineapple"))




