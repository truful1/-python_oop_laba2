import datetime


class Zate:
    def __init__(self, year, month, day):
        self.date = datetime.date(year, month, day)

    def get_year(self):
        return self.date.year

    def get_month(self):
        return self.date.month

    def get_day(self):
        return self.date.day

    def get_day_of_week(self):
        return self.date.weekday()

    def get_day_name(self):
        days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
        return days[self.get_day_of_week()]

    def get_month_name(self):
        months = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"]
        return months[self.get_month() - 1]

class ZateExt(Zate):

    def add_year(self, year):
        return f'{self.date.year + year} {self.date.month} {self.date.day}'

    def minus_year(self, year):
        return f'{self.date.year - year} {self.date.month} {self.date.day}'

    def add_mounth(self, mounth):
        return f'{self.date.year} {self.date.month + mounth} {self.date.day}'

    def minus_mounth(self, mounth):
        return f'{self.date.year} {self.date.month - mounth} {self.date.day}'

