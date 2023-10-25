class Rectangle:
    __height = None
    __width = None

    def __init__(self, h, w):

        self.__height = h
        self.__width = w

    def getSquare(self):
        return self.__width * self.__height
