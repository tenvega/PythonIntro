#  String Functions

myStr = "Hello there World!"

# Capitalize
print(myStr.capitalize())

# Swap case
print(myStr.swapcase())

# Get Length

print(len(myStr))

# replace
print(myStr.replace('World', 'Everyone'))

# count
sub = "l"
print(myStr.count(sub))

# Startswith
print(myStr.startswith('Hello'))

print(myStr.endswith('World!'))

# Split to myList
print(myStr.split())

# find
print(myStr.find('World'))

# index
print(myStr.index('H'))

# Is all alphanumeric
print(myStr.isalnum())

# Is all alphabetic
print(myStr.isalpha())

# Is all digit instead of numeric
print(myStr.isdigit())
