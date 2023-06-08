# i = 3
# while i != 0:
#     print('meow')
#     i -= 1

# for i in [0, 1, 2]:
#     print('meow')

# for _ in range(7):
#     print('meow')

# print('meow\n' * 3, end='')

# while True:
#     n = int(input('What\'s n?: '))
#     if n > 0:
#         break

# for _ in range(n):
#     print('meow')

def main():
    x = get_number()
    meow(x)


def get_number():
    while True:
        n = int(input('What\'s n?: '))
        if n > 0:
            return n


def meow(n):
    for _ in range(n):
        print('meow')


main()
