class Student:
    name = "John"
    surname = "Doe"

    def show(self):
        return f"Name: {self.name}, Surname: {self.surname}"

student = Student()
print(student.show())