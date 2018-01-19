# Open a file

fo = open('test.txt', 'w')

# Get some info
print('Name: ', fo.name)
print('Is Closed: ', fo.closed)
print('Opening Mode: ', fo.mode)

# Write to file
fo.write('I love Python')
fo.write(' and javascript')

# Close file
fo.close()

# Open to append
fo = open('test.txt', 'a')
fo.write(' I also like PHP.')

# read from file
fo = open('test.txt', 'r+')
text = fo.read(10)
print(text)
fo.close()

# Create file
fo = open('test2.text', 'w+')
fo.write('This is my new file')
fo.close()
