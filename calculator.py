def main():
    x = (input('What\'s x: '))
    print(f'Square of {x} is: ', square(x))


def square(n):
    return pow(n, 2)
    # return n*n


if __name__ == '__main__': 
  main()
