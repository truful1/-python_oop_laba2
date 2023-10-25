class User:
    __name = None

    def __setName(self, name):
        self.__name = name

    def __getName(self):
        return self.__name


class Employee(User):
    def __setName(self, name):
        if (len(name) > 0):
            self.__name = name