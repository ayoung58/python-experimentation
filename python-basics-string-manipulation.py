# Can use \ as escape character
# if you add r in front of quotes, it becomes a raw string (so backslashes would also be printed)

print(r"C:\yes\ma'am")
# If you want a string message to be multiline, you can use triple quotes '''
'''multiline string is 
used for comments that span
multiple lines :)'''

# String manipulation:
bob = "Mynameisbob"
# Start, end (not included), step size
print(bob[2:5:1])
# return every other
print(bob[::2])

# To trim, use .strip(). By default, removes whitespace, but if you add characters inside parentheses, will remove those
# lstrip and rstrip removes from only the left and right, respectively.

testWord = "yyxxyyHelloyyxxyy"
testWordEdited = testWord.strip("xy") # Outputs Hello
print(testWordEdited)

# To add padding, use ljust() and rjust(). First argument: length of result string, NOT length of padding. 
# Second argument: what character you want to pad with
# ljust adds padding to right, rjust adds to left. center() adds to both!
noPadding = "Hello"
padded = noPadding.rjust(10, "x") + noPadding.ljust(10, "y")[5:]
paddedMore = padded.center(25, "=")
print(paddedMore)
# This is great for organizing information so that it looks presentable in console (can align all with padding)
''' Example
-------PICNIC ITEMS-------
sandwiches..........     4
apples..............    12
cups................     4
'''

# Can use "in" and "not in" to see if a particular string is contained in another

name = 'Al'
age = 4000
# string interpolation (a little older than f-strings)
print('My name is %s. I am %s years old.' % (name, age))
# f-strings (remember the f)
print(f'My name is {name}. Next year I will be {age + 1}.')

# use .lower() and .upper() to convert to lower and upper cases
# islower() and isupper() will return a boolean

# Other useful isX() methods:
'''
isalpha() Returns True if the string consists only of letters and isn’t blank
isalnum() Returns True if the string consists only of letters and numbers and is not blank
isdecimal() Returns True if the string consists only of numeric characters and is not blank
isspace() Returns True if the string consists only of spaces, tabs, and newlines and is not blank
istitle() Returns True if the string consists only of words that begin with an uppercase letter followed by only lowercase letters
'''
# startswith() and endswith() returns true if string value they are called with starts/ends with string in parentheses

# .join() takes a list and concatenates the strings with the string it is called with
print(', '.join(['cats', 'rats', 'bats']))
# split() takes string and splits it into a list
print('MyABCnameABCisABCSimon'.split('ABC'))   
# Can use split() to split a multiline string into a list with each element as one line (.split("\n"))
# partition() splits a string into a tuple so that it contains: “before,” “separator,” and “after”
# If can't find the separator in the string, then does: "string", "", ""
# If there's more than one of the separator, partition() will use the first one
# Can use multiple assignment trick:
before, sep, after = 'Hello, world!'.partition(' ')
print(before)