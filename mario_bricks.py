def main():
    print_square(3),
    print_column(0),
    print_row(0)


def print_column(height):
    for _ in range(height):
        print('#\n', end='')


def print_row(width):
    print('?'*width)


def print_square(size):
    for i in range(size):
        print('?'*size)


main()
