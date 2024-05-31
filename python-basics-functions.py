def hello(name):
    return "hello " + name
    
print("Please type name: ")
myName = input()
print(hello(myName))

# Since print function does not return anything, hi stores nothing
# end is a keyword argument (much like in CSS), and modifies
# what comes after the printed line
hi = print("hello", end=" ")
if None == hi:
    print("True")

# Can print multiple things, and can change the separator
print("bob", "Alice", "john", sep=" + ")
