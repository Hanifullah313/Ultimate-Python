items = ["apple", "banana", "cherry" , 25, True , 5.5]
print("Original List:", items)
print("First Item:", items[0])
print("Last Item:", items[-1])
print("Slice (1-3):", items[1:4])
items[0] = "orange"
print("Modified List:", items)  
items.append("grape")
print("After Append:", items)


# list methods
items.insert(1, "kiwi")
print("After Insert:", items)
items.remove("banana")
print("After Remove:", items)
popped_item = items.pop()
print("Popped Item:", popped_item)
# difference between remove and pop ?
# remove() removes the first occurrence of a specified value, while pop() removes an item at a specified index (or the last item if no index is provided) and returns it.
print("After Pop:", items)
items.sort(key=str)
# what is key=str in sort method ?
# The key=str argument in the sort() method specifies that the sorting should be done based on the string representation of the items. This is useful when the list contains mixed data types.
print("After Sort:", items)

items.reverse()
print("After Reverse:", items)