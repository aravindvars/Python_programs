import csv

family = [] # define an empty list

with open('family.csv') as file:  
  reader = csv.DictReader(file)
  for row in reader:
    family.append(row) # append this dictionary to the list defined earlier
    

for individual in sorted(family, key=lambda individual: individual['name']): 
  print(f'{individual["name"]} : {individual["occupation"]}: {individual["age"]}')

