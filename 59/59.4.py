class Month:
    def __init__(self, month_number):
        if 1 <= month_number <= 12:
            self.month_number = month_number
        else:
            raise ValueError("Номер месяца должен быть от 1 до 12")

    def get_month_number(self):
        return self.month_number

    def get_month_name(self):
        months = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"]
        return months[self.month_number - 1]

    def get_last_day_of_month(self):
        if self.month_number in {1, 3, 5, 7, 8, 10, 12}:
            return 31
        elif self.month_number in {4, 6, 9, 11}:
            return 30
        else:
            return 29 if self.is_leap_year() else 28

