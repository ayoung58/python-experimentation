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
