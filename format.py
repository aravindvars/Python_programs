import re

name = input('What\'s your name?: ').strip()
if matches := re.search(r'^(.+), *(.+)$', name): # re.search actually returns a value and we are storing that in a matches variable
    name = matches.group(2) + ' ' + matches.group(1)
    
# if matches:
  # first = matches.group(2)
  # last = matches.group(1)
  # name = f'{first} {last}'
  
print(f'Hello, {name}')