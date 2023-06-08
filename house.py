name = input('What\'s your name: ')

match name:
    case 'Harry' | 'Ron' | 'Hermoine':
        print('x')
    case 'Draco':
        print('y')
    case _:
        print('Who?')
