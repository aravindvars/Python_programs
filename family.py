import csv

family = [] # define an empty list

with open('family.csv') as file:  
  reader = csv.reader(file)
  for name, occupation, age in reader:
    # name, occupation, age = line.rstrip().split(',')  # split the values inside the fileinto diff variables
    # individual = {'name':name, 'occupation':occupation, 'age':age} # define a dictionary with keys that will hold data for the list
    family.append({'name': name, 'occupation': occupation, 'age': age}) # append this dictionary to the list defined earlier, not the file
    
# def get_name(individual):
#   return individual['name']

for individual in sorted(family, key=lambda individual: individual['name']): # key here is defined using a lambda function. lambda means anonymous, which means we need not name the function sice we are not suing it anywhere again
  print(f'{individual["name"]} : {individual["occupation"]}: {individual["age"]}')

# for individual in sorted(family, key=get_name): #sort the list and using a key inside the dictionary
#   print(f'{individual["name"]} : {individual["occupation"]}')
    
    
    
# print(f'{name}\'s Occupation is {occupation} and their age is {age}')