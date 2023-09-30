students = ["Hermion", "Harry", "Ron"]

print(students[0])
print(students[1])
print(students[2]);

students = ["Hermion", "Harry", "Ron"]
for student in students:
    print(student);

students = ["Hermion", "Harry", "Ron"]
for i in range(len(students)):
    print(i + 1 ,students[i]);

students = [
    {"name": "ahmed", "house" : "cairo", "university" : "Helwan"},
    {"name": "mahmoud", "house" : "ismalya", "university" : "cairo"},
    {"name": "amal", "house" : "giza", "university" : "ain shames"},
    {"name": "faten", "house" : "monofya", "university" : "sinaii"}
]

for i in students:
    print(i["name"], i["house"], i["university"], sep=", ")