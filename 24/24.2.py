class Employee:
    __name = None
    __salary = None

    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary

    def getInfo(self):
        return self.__name, self.__salary

stuffs = [
    Employee('Александр', 64500),
    Employee('Ирина', 18000),
    Employee('Максим', 123765)
]

for i in stuffs:
    print(i.getInfo())