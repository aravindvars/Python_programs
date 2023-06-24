# name = input ('What\'s your name:')


# file = open('names.txt', 'w') # 'w' will re-write the contents whenever the program is run. It doesn't append
# with open('names.txt', 'a') as file:  # appending the new character
#   file.write(f'{name}\n')
#file.close() #file.close() can be circumvented by using with keyword as shown above

names = []
with open ('names.txt') as file:
  for line in file:
    names.append(line.rstrip())

for name in sorted(names, reverse=True):
  print(f'hello, {name}' )

# with open ('names.txt') as file:
#   for line in sorted(file):
#     print(f'hello,', line.rstrip())


#   lines = file2.readlines()

# for line in lines:
#   print(f'hello,',line.rstrip()) # rstrip() strips of the extra lines in the file



# for _ in range(3):
#   name = input ('What\'s your name:')
#   names.append(name)

# for name in sorted(names):
#   print(f'hello, {name}')