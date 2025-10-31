# what is set in python
# sets are unordered collections of unique elements. They are defined using curly braces {} or the set() function.
# sets are mutable, meaning you can add or remove elements after creation.
my_set = {1, 2, 3, 4, 5}
print("Original Set:", my_set)

# methods of sets
my_set.add(6)
print("After Adding 6:", my_set)

my_set.remove(2)
print("After Removing 2:", my_set)

print("Is 3 in the set?", 3 in my_set)


# Operations on set 
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
# Union
set_union = set_a.union(set_b)
print("Union of A and B:", set_union)

# Intersection
set_intersection = set_a.intersection(set_b)
print("Intersection of A and B:", set_intersection)

# Difference
set_difference = set_a.difference(set_b)
print("Difference of A and B:", set_difference)

# Symmetric Difference
set_symmetric_difference = set_a.symmetric_difference(set_b)
print("Symmetric Difference of A and B:", set_symmetric_difference)

# what is set_symmetric_difference
# The symmetric difference of two sets is a set that contains elements that are in either of the sets but not in their intersection. In other words, it includes elements that are unique to each set.

# clear , remove , lens
print("Length of set_a:", len(set_a))
set_a.clear()   
print("After Clearing set_a:", set_a)
set_b.remove(5)
print("After Removing 5 from set_b:", set_b)