from datetime import  datetime

class Zate:

    def __init__(self, y, m, d):
        self.day = d
        self.mounth = m
        self.year = y

    def getYear(self):
        return self.year

    def getMounth(self):
        return self.mounth

    def getDay(self):
        return self.day