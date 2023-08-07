class Student: 
    def __init__(self, name, house):
      self.name = name
      self.house = house
      
    
    def __str__(self):
      return f'{self.name} from {self.house}' 
    
    # @property
    # def name(self):
    #     return self.name
    
    # @name.setter
    # def name(self, name):
    #     if not name:
    #         raise ValueError('Missing Name')


    # #Getter function
    # @property
    # def house(self):
    #   return self.house
    
    # #Setter fucntion --> This is used to prevent the programmer to change attributes which we don't wanr to allow for change
    # @house.setter
    # def house(self, house):
    #   if house not in ['Gryffindor', 'Hufflepuff', 'Ravenclaw', 'Slytherin']:
    #     raise ValueError ('Invalid House name')
    #   self._house = house # The instance variable is used with an underscore.
    
    @classmethod  
    def get(cls):
        name = input('Name: ')
        house = input('House: ')
        return cls(name,house) 
  

def main():
    student = Student.get()
    print(student) 
  
if __name__ == '__main__':
  main()
  