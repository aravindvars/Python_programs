marks = int(input('Student\'s mark is:'))

if 90 <= marks <= 100:
    print('S grade')
elif 80 <= marks < 90:
    print('A grade')
elif 70 <= marks < 80:
    print('B grade')
elif 60 <= marks < 70:
    print('C grade')
elif 50 <= marks < 60:
    print('D grade')
elif 40 <= marks < 50:
    print('E grade')
else:
    print('F grade')
