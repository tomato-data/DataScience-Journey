class Student():
    def study(self):
        print("study")

class Teacher:
    def teach(self):
        print("teach")

classroom = [Student(), Student(), Teacher(), Student(), Student()]

for person in classroom:
    if isinstance(person, Student):
        person.study()
    elif isinstance(person, Teacher):
        person.teach()
    