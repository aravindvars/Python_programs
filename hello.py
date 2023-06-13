def main():
    name = input('What\'s your name?: ')
    print(hello(name))


def hello(to='world'):
    return f'hello {to}'   #assert statements are usually designed to test return values rather than side effects like print

if __name__ == '__main__':
    main()
