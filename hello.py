#Ask user for their name and print it
name = input('What\'s your name?: ').strip().title() #Remove Whitespace from str & capitalize the first letter

# Split user name into first & last
first, last = name.split(' ')
print(f'hello, {first}') # The sepearator has default single space




