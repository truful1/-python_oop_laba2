class Employee:
    __name = None
    __salary = None

    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary

stuffs = [
    Employee('Александр', 64500),
    Employee('Ирина', 18000),
    Employee('Максим', 123765)
]
