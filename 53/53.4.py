class Circle:
    __radius = None

    def __init__(self, r: float):
        self.__radius = r

    def squareCircle(self):
        return 3.14 * (self.__radius ** 2)

    def lenCircle(self):
        return 3.14 * self.__radius * 2

circle = Circle(1.1)

print(circle.lenCircle())
print(circle.squareCircle())