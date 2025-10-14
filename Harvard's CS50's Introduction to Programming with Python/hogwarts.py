students = [
    {"name": "Hermione Granger", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry Potter", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron Weasley", "house": "Gryffindor", "patronus": "Jack Russell Terrier"},
    {"name": "Draco Malfoy", "house": "Slytherin", "patronus": None},
]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")