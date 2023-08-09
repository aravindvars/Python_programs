class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError('Missing Name')
        self.name = name
        

class Student(Wizard): #Inheritance
    def __init__(self,name,house):
        super().__init__(name)
        self.house = house
    
    def __str__(self):
        return f'{self.name} is from {self.house}'

class Professor(Wizard):
    def __init__(self, name,subject):
        super().__init__(name)
        self.subject = subject
    
    def __str__(self):
        return f'{self.name} teaches {self.subject}'


def main():
    student = Student('Harry', 'Gryffindor')
    print(student)
    professor = Professor('Snape', 'Defense')
    print(professor)
    
if __name__ == '__main__':
    main()