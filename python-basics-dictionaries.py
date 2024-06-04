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