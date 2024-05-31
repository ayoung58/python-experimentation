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

# can make a local variable global like this if truly want to 
def definingGlobal():
    global bob
    
def argumentsTrial(num):
    num += 3

num = 5
argumentsTrial(num)
# variable passed in does not change after the function performs on the parameter
print(num)
    
def erroring():
    # If there are multiple lines in the try block, the lines after the line with a 
    # problem will not execute
    try:
        return 42/0
    # needs to define what the error is
    except ZeroDivisionError:
        print("Error!")

# Can import time and use time.sleep(___) to pause a program for a given number of seconds
