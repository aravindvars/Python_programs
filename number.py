def main():
    x = get_int('What\'s X?: ')
    print(f'X is {x}')


def get_int(message):
    while True:
        try:
            return int(input(message))
        except ValueError:
            pass
            # print('The value you typed is not an integer. Please try again !!')
        # else:
        #     return x


main()

# x = (input('What\'s X?: '))

# if (x.isdigit()):
#     x = int(x)
#     print(f'X is {x*2}')
# else:
#     print('Enter an Integer')
