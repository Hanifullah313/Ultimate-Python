age = int(input("Enter your age: "))
if age > 18 :
    print("you can vote")

elif age < 18 and age > 0:
    print("you are a minor.")
else :
    print("Invalid age entered.")    