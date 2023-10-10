class Employee:
    def __init__(self, name, salary, age):
        self.__name = name
        self.__salary = salary
        self.__age = age

    def show_info(self):
        return f"Name: {self.__name}, Salary: {self.__salary}, Age: {self.__age}"

employee = Employee("John Doe", 5000, 30)

print(employee.show_info())