class User:
    name = None
    surname = None


class Employee:
    pass


class Employee(User):
    pass


worker = Employee()
worker.name = "Jack"
worker.surname = "Milt"
print("Имя:", worker.name, "\nФамилия:", worker.surname)
