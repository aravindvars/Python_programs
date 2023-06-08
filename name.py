import sys

if len(sys.argv) < 4:
    sys.exit('Too few arguments')

for arg in sys.argv[1:-1]:
    print('hello, my name is', arg)
# elif len(sys.argv) > 4:
#     sys.exit('Too many')


# print('hello, my name is', sys.argv[1], sys.argv[3])


# try:
#
# except IndexError:
#     print('You haven\'t given the argument')
