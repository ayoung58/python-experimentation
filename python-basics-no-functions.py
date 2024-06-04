import random, sys, os, math

print("hello world")
print("enter name:")

myName = input()
print("hi " + myName)

print("length of name: " + str(len(myName)))

if myName == "bob":
    print("twinsies!")
elif len(myName) > 3:
    print("long name bro.")
elif myName == "exit":
    # terminates the program early, but only works with IDLE (probably not in a terminal)
    sys.exit()
else:
    print("nah man.")
    
counter = 3
while counter > 0:
    print("counting down")
    print(counter)
    counter -= 1
    if counter == 2:
        continue
    counter -= 2
print(counter)

# last number of the three is how much to step by each time
for i in range(12, 15, 1):
    print(i)
    
for i in range(3):
    print(random.randint(1, 10))
