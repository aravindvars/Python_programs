import random

class Hat:
  
      houses = ['Gryffindor', 'Hufflepuff', 'Ravenclaw', 'Slytherin'] # houses is now a class varibale and not a instant variable
    
      @classmethod
      def sort(cls, name):
            house = random.choice(cls.houses)
            print(name, 'is in', house)

# hat = Hat() Now we need not instantiate the hat object to a class Hat. We can directly refer the class now
Hat.sort('Harry')

      
      
      
      
      
      
      
  
