# Dictionaries are mutable and unordered (unlike lists)
# Can still access via index (the keys as index), but when comparing two dictionaries, 
# A == B even if in different orders
# Since no order, cannot be sliced

# To access value, use the key as the "index":

birthdays = {"Bob": 'Apr 1', "Joey": 'May 1', "Alicia": 'June 1'}
name = "Bob"

if name in birthdays:
    print(birthdays[name] + " is the birthday of " + name)
else:
    print("not in dictionary.")
    
# To add into dictionary
birthdays["Nicky"] = "Sept 1"
print(birthdays["Nicky"])
# setdefault() can do this in one line though. If exists, returns value. If doesn't, sets and returns. 
birthdays.setdefault("Nicky", "Dec 1")

# Can use for loop to loop through all keys or values:
for v in birthdays.values():
    print(v)
    
for v in birthdays.keys():
    print(v)

# .items() returns key value pairs as tuples
for v in birthdays.items():
    print(v)
    
# or
for k, v in birthdays.items():
    print("Key: " + k + ", Value: " + v)
    
# Can also wrap birthdays.keys() in list() to get a true list
# Use the .get() method to retrieve a key (second value is returned if there's no key)
# Using the index method would give an error if there's no key, so use this method instead.

print(birthdays.get("Alicia", "not recorded."))
print(birthdays.get("Martha", "not recorded."))

# Program that counts the characters in a sentence:
message = "the quick brown fox jumps over the lazy dog."
count = {}

for character in message:
    # If there isn't that character, then initialize it with 0 so that 
    # the next line can add 1 to it
    # Else, if there is that character, this line will do nothing, and the 
    # next line will add 1 to the existing value.
    count.setdefault(character, 0)
    count[character] = count[character] + 1
    
countList = list(count.keys())
countList.sort(key=str.lower)
for i in countList:
    print("'" + i + "'" + ": " + str(count[i]), end=", ")
print("\n")

# Dictionaries have a lot of uses, from Chess with algebraic notation, to tic tac toe

# Nested dictionaries/lists example: 
allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
             'Bob': {'ham sandwiches': 3, 'apples': 2},
             'Carol': {'cups': 3, 'apple pies': 1}}
def totalBrought(guests, item):
    numBrought = 0
    # goes through each key value pair, mainly needing the values, which are dictionaries themselves
    for k, v in guests.items():
        # tries to get the value with the item fed in as parameter, 
        # but if there isn't, then adds 0 to numBrought
        numBrought = numBrought + v.get(item, 0)
    # After going through every key value pair (basically, every guest), returns
    # the total number of the item that is brought.
    return numBrought

print(' - Apples         ' + str(totalBrought(allGuests, 'apples')))
print(' - Cups           ' + str(totalBrought(allGuests, 'cups')))
