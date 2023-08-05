class Student: # class is a blueprint, a mould. A class can be termed as a data type that we have created in our code to match our requirements
  ...


def main():
  student = get_student()
  print(f'{student.name} from {student.house}')
  

def get_student():
  student = Student() # object is when you use the mould to build something
  student.name = input('Name: ')
  student.house = input('House: ')
  return student


if __name__ == '__main__':
  main()
  