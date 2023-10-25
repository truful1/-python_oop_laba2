class User:
    def setName(self, name):
        if (self.notEmpty(name)):
            self.name = name

    def getName(self):
        return self.name

    def __notEmpty(stri):
        return len(stri) > 0


class Employee(User):
    def setSurn(self, surname):
        if (self.notEmpty(surname)):
            self.surname = surname

    def getSurn(self):
        return self.surname