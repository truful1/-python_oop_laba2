class Circle:
    __radius = None

    def __init__(self, r: float):
        self.__radius = r

    def squareCircle(self):
        return 3.14 * (self.__radius ** 2)

