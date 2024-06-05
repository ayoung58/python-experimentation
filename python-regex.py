import re

# Regex is used for pattern recognition
# i.e. phone numbers:
# remember, r is for raw string, needed since there's so many backslashes
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
# search returns None if no match, and returns a Match object if there is a match
# group() is used on the match object to generate the matched string
mo = phoneNumRegex.search('My number is 416-777-9999')
print("Phone number found: " + mo.group())
noMo = phoneNumRegex.search("Hehe no number")
# This generates an error because .group() cannot be operated on a NoneType
# print("Phone number found: " + noMo.group())

# The parentheses added in the string creates groups
# To access one of these groups, use group(<int>), and to access all in a tuple, use groups()
print(mo.group(0)) # same as group()
print(mo.group(1))
print(mo.group(2))
areaCode, mainNumber = mo.groups()
print(f'Area code: {areaCode}, Main number: {mainNumber}')

# If you want to detect actual parentheses, you again need backslashes
# Key: \.  \^  \$  \*  \+  \?  \{  \}  \[  \]  \\  \|  \(  \)

# Use | to match multiple (like the "or" statement)
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo2 = batRegex.search('Batmobile lost a wheel')
print(mo2.group())
print(mo2.group(1)) # returns what was found in first parentheses group

# Use ? for 0 or 1 occurences of the group in front
# Use * for 0 or more occurences of the group in front
# Use + for 1 or more occurences of the group in front
# Use {} for specific number of occurences (i.e. (h){3, 5} matches hhh, hhhh, hhhhh)
# Without ? behind {} is called greedy matching, which means it takes the longest string possible in ambiguous cases
# {}? takes shortest (i.e. for hhhhh, with {} returns hhhhhh, but with {}? returns hhh)

# .findall() will find all occurences and return a list of strings IF THERE ARE NO GROUPS
# If there are groups, then findall() will return a list of tuples. Each tuple represents a found match, 
# and its items are the matched strings for each group in the regex

print(phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000'))

# Key for character classes/shorthands:
# \d: any numeric digit
# \D: any NON numeric digit
# \w: Any letter, numeric digit, or the underscore character (to match "word" characters)
# \W: Any character that is not a letter, numeric digit, or the underscore character.
# \s: Any space, tab, or newline character
# \S: Any character that is not space, tab, or newline character

# Use [] for own character classes, i.e. [A-E0-9] 
# Inside [], do not need backslash for special characters 
# Use ^ inside [] to return everything NOT in [] (i.e. [^aeiouy] means no vowels)

# Use ^ at the start of a regex to indicate that match must occur at BEGINNING of search text
# Use $ at the end fo a regex to indicate that match must occur at END of search text

# Use . for "wildcard" (will match any character except for newline). To match actual dot, use \.
# Use .* to stand for ANYTHING (basically, any character, any number of times)
# The above uses greedy-mode (match as much text as possible). For non-greedy, use .*?
# re.compile('.*', re.DOTALL): the re.DOTALL matches even newline characters 

nongreedyRegex = re.compile(r'<.*?>')
mo3 = nongreedyRegex.search('<To serve man> for dinner.>')
print(mo3.group())
greedyRegex = re.compile(r'<.*>')
mo4 = greedyRegex.search('<To serve man> for dinner.>')
print(mo4.group())

# Using a second argument of re.I will IGNORE CASE
# Using .sub on a Match Object will substitute found matches in the second argument with the first argument string
namesRegex = re.compile(r'Agent \w+')
print(namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.'))

# If you want to use the matched text itself in the substitution, then you can use \1, \2, etc. 
# for group 1, group 2, etc.
agentNamesRegex = re.compile(r'Agent (\w)\w*')
print(agentNamesRegex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.'))
# Since group 1 is the first letter of the agent's name, that gives us the first letter and then **** after.

# To organize more complex matches, you can use multiline, but need to include re.VERBOSE so that
# re.compile ignores whitespace.
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?            # area code
    (\s|-|\.)?                    # separator
    \d{3}                         # first 3 digits
    (\s|-|\.)                     # separator
    \d{4}                         # last 4 digits
    (\s*(ext|x|ext.)\s*\d{2,5})?  # extension
    )''', re.VERBOSE)

# For more than one second argument, use the pipe | character, i.e. re.VERBOSE | re.DOTALL
