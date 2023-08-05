


def main():
  student = get_student()
  if student['name'] == 'Padma':
    student['house'] = 'Ravenclaw'
  print(f'{student["name"]} from {student["house"]}')

def get_student():
  name = input('Name: ')
  house = input('House: ')
  return {'name': name, 'house': house}

  # return (name, house) # This is a TUPLE. Tuples are immutable in sense you can't change the values of a tuple after declared where as a list are mutable meaning you can change the values of a list


if __name__ == '__main__':
  main()
  