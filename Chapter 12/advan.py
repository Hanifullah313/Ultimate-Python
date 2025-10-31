# what is walrus operator in python
# The walrus operator (:=) in Python is used to assign values to variables as part of an expression. It allows you to both assign a value to a variable and return that value in a single line of code.
# Example without walrus operator
n = len("Hello, World!")
if n > 5:
    print("Long string")
else:
    print("Short string")
   # Example with walrus operator
if (n := len("Hello, World!")) > 5:
    print("Long string")
else:
    print("Short string")





# what is match case in python
# The match-case statement in Python is a control flow structure that allows you to match a value against a series of patterns and execute corresponding code blocks based on the match. It was introduced in Python 3.10 as a more powerful alternative to traditional if-elif-else statements for certain use cases.
def http_status(status_code):
    match status_code:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case 500:
            return "Internal Server Error"
        case _:
            return "Unknown Status Code"