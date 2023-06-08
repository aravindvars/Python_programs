# students = ['Hermoine', 'Harry', 'Ron', 'Draco']
# houses = ['Gr', 'Gr', 'Gr', 'Sl']
students = {  # This is a key:value pair
    'Hermoine': 'Gr',
    'Harry': 'Gr',
    'Ron': 'Gr',
    'Draco': 'Sl'
}
for student in students:
    print(student, students[student], sep=', House:')

# for i in range(len(students)):
#     print(i+1, students[i])

# print(students['Hermoine'])
