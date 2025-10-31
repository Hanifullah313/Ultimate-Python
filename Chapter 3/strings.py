#strings
name = "Hanif"
print("Name:", name)
print("Uppercase:", name.upper())
print("Lowercase:", name.lower())
print("Titlecase:", name.title())
print("Length:", len(name))
print("Replace 'a' with 'o':", name.replace('a', 'o'))
# how string is immutable ?
# Strings are immutable, meaning once they are created, their characters cannot be changed individually. Any modification creates a new string.
# when we replace a character in string a new string is created
# in concatenation new string is created
print("Find 'n':", name.find('n'))
print("Split by 'i':", name.split('i'))
print("Concatenate:", name + " Ullah")
print("Formatted String: Hello, {}!".format(name))
print(f"F-String: Hello, {name}!")
print("Is Alphabetic:", name.isalpha())
print("Is Numeric:", name.isnumeric())
print("Is Alphanumeric:", name.isalnum())
print("Strip 'H':", name.strip('H'))
print("Count 'a':", name.count('a'))
print("Starts with 'H':", name.startswith('H'))
print("Ends with 'f':", name.endswith('f'))
short_name = name[0:3]
print("Sliced Name (0-3):", short_name)
print("negative slicing -1:", name[-4:-1])
print("reverse string:", name[::-1])
# how reverse string works ?
# In Python, slicing with a negative step (e.g., [::-1]) starts from the end of the string and moves backwards, effectively reversing the string.

# escape sequences
print("New Line:\nHello")
print("Tab:\tHello")
print("Backslash:\\Hello")
print("Single Quote:\'Hello\'")
print("Double Quote:\"Hello\"")
print("Carriage Return:\rHello")
print("Bell Sound:\aHello")




# chaining methods
chained = name.strip('H').upper().replace('A', 'O')
print("Chained Methods:", chained)

# detecting double spaces
text = "This  is  a  test."
double_spaces = text.count("  ")
print("Double Spaces Count:", double_spaces)