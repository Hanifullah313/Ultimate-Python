for i in range(0,4):
    print("Iteration:", i)


# While Loop

i = 1
while i <= 5 :
    print("While Loop Iteration:", i)
    i += 1



# What is for loop with else 
# In Python, a for loop can have an else clause that executes after the loop completes normally (i.e., not terminated by a break statement). The else block runs when the loop has iterated over all items in the sequence.

for i in range(0,10):
    print(i)

else :
    print("loop terminated")



# break and continue
for i in range(0,10):
    if i == 4 :
        break
    print(i)

else :
    print("loop terminated")
 
for i in range(0,10):
    if i == 4 :
        continue
    print(i)

else :
    print("loop terminated")
 