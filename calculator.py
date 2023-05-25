x = float(input("Enter the value of X: ")) # Int is not just a data type in python instead it's also a function
y = float(input("Enter the value of Y: "))

z= round(x+y)
A = x / y
print(f'Sum of both the numbers rounded off is {z:,}', sep='')
print(f'{A:.2f}')
