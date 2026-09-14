class Student:
    school_name = "Oxford"

    def __init__(self, name):
        self.name = name


student1 = Student("Alice")
student2 = Student("Bob")

print(student1.name, student1.__class__.school_name)  # Alice Oxford
print(student2.name, student2.__class__.school_name)  # Bob Oxford
