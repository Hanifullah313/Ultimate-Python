# what is dictionary in python
my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
print("Original Dictionary:", my_dict)
# Accessing values  
print("Name:", my_dict["name"])
print("Age:", my_dict.get("age"))
print("City:", my_dict.get("city"))
# Adding a new key-value pair
my_dict["job"] = "Engineer"
print("After Adding Job:", my_dict)
# Modifying an existing value
my_dict["age"] = 31
print("After Modifying Age:", my_dict)