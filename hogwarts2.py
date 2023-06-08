students = [
    {'name': 'Hermoine', 'house': 'Gr', 'patronous': 'Otter'},
    {'name': 'Harry', 'house': 'Gr', 'patronous': 'Stag'},
    {'name': 'Ron', 'house': 'Gr', 'patronous': 'Terrier'},
    {'name': 'Draco', 'house': 'Gr', 'patronous': None}
    # None here is equivalent of NULL...meaning no value
]

for student in students:
    print(student['name'], student['house'], student['patronous'], sep=':')
