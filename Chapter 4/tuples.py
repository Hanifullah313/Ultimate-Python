# what is Tuples in Python
# Tuples are ordered, immutable collections of items. They are similar to lists but cannot be modified after creation.
# Tuples are defined using parentheses ().
items = ("apple", "banana", "cherry" , 25, True , 5.5)
print("Original Tuple:", items)
print("First Item:", items[0])
print("Last Item:", items[-1])
print("Slice (1-3):", items[1:4])

# Methods applicable to tuples
print("Count of 'apple':", items.count("apple"))
print("Index of 'cherry':", items.index("cherry"))
# why tuples are immutable ?
# Tuples are immutable to ensure data integrity and to allow for optimizations in memory usage and performance. This immutability makes tuples suitable for use as keys in dictionaries and elements in sets, which require hashable types.
# trying to modify a tuple will raise an error
# items[0] = "orange"  # This will raise a TypeError
# however we can concatenate tuples to create a new tuple
new_items = items + ("orange", "grape")
print("New Tuple:", new_items)