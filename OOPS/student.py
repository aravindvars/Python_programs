class Student: 
    def __init__(self, name, house):
      self.name = name
      self.house = house
      
    
    def __str__(self):
      return f'{self.name} from {self.house}' 
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError('Missing Name')


    #Getter function
    @property
    def house(self):
      return self._house
    
    #Setter fucntion --> This is used to prevent the programmer to change attributes which we don't wanr to allow for change
    @house.setter
    def house(self, house):
      if house not in ['Gryffindor', 'Hufflepuff', 'Ravenclaw', 'Slytherin']:
        raise ValueError ('Invalid House name')
      self._house = house # The instance variable is used with an underscore.
  

def main():
    student = get_student()
    #student.house = 'Green'  Now this will not happen as we set the setter function to prevent
    print(student) 
  
  

def get_student():
  name = input('Name: ')
  house = input('House: ')
  return Student(name,house) 
  

if __name__ == '__main__':
  main()
  