from datetime import datetime

class Period:

    def __init__(self, start_time, end_time):
        self.start = start_time
        self.end = end_time

    def getSecond(self):
        result = int( (self.end - self.start).total_second() )

        return result

    def getMinutes(self):
        return self.getSecond() // 60


