class Student: 
    def __init__(self, name, house): # __init__ is the inititalization of the object in python. "New" method of python creates the object, which runs in the background and this init method initialises it. We as a programmer need to worry about the init method only. Python takes care of new
      if not name:
        raise ValueError('Missing Name')
      if house not in ['Gryffindor', 'Hufflepuff', 'Ravenclaw', 'Slytherin']:
        raise ValueError("House name Invalid")
      self.name = name
      self.house = house
    
    
    def __str__(self):
      return f'{self.name} from {self.house}' # This __str__ gets called when the object location is called.
  


def main():
  student = get_student()
  print(student) # This references the object in the memory and print out it's location
  

def get_student():
  name = input('Name: ')
  house = input('House: ')
  return Student(name,house) # This is a constructor call. This is going to construct a student object for us. student object is created by using the Student class as template
  


if __name__ == '__main__':
  main()
  