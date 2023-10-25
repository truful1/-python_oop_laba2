class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


class EmployeesCollection:
    def __init__(self):
        self.employees = []


class EmployeesCollection:
    def __init__(self):
        self.employees = []

    def add_employee(self, name, salary):
        new_employee = Employee(name, salary)
        self.employees.append(new_employee)

    def list_employees(self):
        for employee in self.employees:
            print(f"Имя: {employee.name}, Зарплата: {employee.salary}")

class EmployeesCollection:
    def __init__(self):
        self.employees = []

    def add_employee(self, name, salary):
        new_employee = Employee(name, salary)
        self.employees.append(new_employee)

    def list_employees(self):
        for employee in self.employees:
            print(f"Имя: {employee.name}, Зарплата: {employee.salary}")

    def total_salary(self):
        total = sum(employee.salary for employee in self.employees)
        return total

class EmployeesCollection:
    def __init__(self):
        self.employees = []

    def add_employee(self, name, salary):
        new_employee = Employee(name, salary)
        self.employees.append(new_employee)

    def list_employees(self):
        for employee in self.employees:
            print(f"Имя: {employee.name}, Зарплата: {employee.salary}")

    def total_salary(self):
        total = sum(employee.salary for employee in self.employees)
        return total
