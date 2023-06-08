def main():
    x = int(input('X:'))
    if isEven(x):
        print('Number is Even')
    else:
        print('Number is odd')


def isEven(n):
    return (n % 2 == 0)


main()
