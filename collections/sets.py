# Sets

utensils = {"fork", "knife", "spoon", "spatula"}
print(utensils, type(utensils))

empty = set()
print(empty, type(empty))

utensils.add('garlic press')
utensils.discard('knife')
print(utensils)

# frozen sets

x = frozenset([1, 2, 4, 6])
print(x, type(x))
