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

