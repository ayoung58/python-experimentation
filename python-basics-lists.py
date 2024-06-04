# Python lists are heterogenous!
demo = [1, 2, 3, 5, 67, [5, "yee", 3, 5]]

print(demo[0])
print(demo[-1])
# Includes 0 but does not include 2
print(demo[0:2])
print(demo[5][2])
print(len(demo))
demo[-3] = "water"
print(demo[-3])
demo[2] = demo[0]
demo[1] = demo[2]
print(demo)
print(demo * 2 + ["1", 2, 4])
# Does not return a value and must take index as argument
del(demo[3])
print(demo)

# Can use a for-each loop by doing for i in [__, __, ...]

# To check if an element is in a list:
print(3 in demo)
print(55 not in demo)

# If you want to assign a variable to every element of a list, then 
# you can use "tuple unpacking" (num of variables must equal num elements)

tupling = [4, 5, 6]
first, second, third = tupling
print(first + second + third)

# Enumeration (returns two values: the index of the item in the list, and the item in the list itself.)

supplies = ['pens', 'staplers', 'flamethrowers', 'binders']
# enumerate returns the index and the item, so we need two variables
for index, item in enumerate(supplies):
    print('Index ' + str(index) + ' in supplies is: ' + item)
    
# random.choice(<list>) randomly selects an item in the list
# random.shuffle(<list>) reorders the list IN ITS PLACE (not a new list!)

# List Operations and Methods (<list>.method())

sampleList = ['h', 's', 'q', 'h', 't']

print(sampleList.index('h')) # only returns the first element found
sampleList.append('l') # adds to end of list
sampleList.insert(2, 'Poop') # adds at given index
print(sampleList)
sampleList.remove('h') # removes the first instance
print(sampleList)
sampleList.sort(reverse=True, key=str.lower) # sorted by ASCII alphabetical order, cannot sort list with multiple types
# If you want to sort based on true alphabetical order, with capital after lower and A before z, then use .sort(key=str.lower)
sampleList.reverse()
print(sampleList)

# Can use the \ character to show that the code extends to next line (and improves readability)

# Tuples: quite similar to lists, except they are IMMUTABLE (cannot have values appended, removed, or modified)
# If only one element, then use comma after, otherwise python thinks it's just one literal element in parentheses.
sampleTuple = ("hello",)
# Convert from tuple to list, list to tuple:
listedTuple = list(sampleTuple)
tupledList = tuple(sampleList)
print(listedTuple)
print(tupledList)
