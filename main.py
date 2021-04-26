class Rectangle:
    def __init__(self, a, b, c, d, x, y, width, height):
        self.__x = x
        self.__y = y
        self.__a = a = [0, 0]
        self.__b = b = [0, y]
        self.__c = c = [x, y]
        self.__d = d = [x, 0]
        self.__width = width = a[0] + d[0]
        self.__height = height = a[1] + b[1]

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if value <= 0:
            raise ValueError("Size of geometric figure must be greater than 0 ")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if value <= 0:
            raise ValueError("Size of geometric figure must be greater than 0 ")
        self.__y = value

    def get_perimeter(self):
        return (self.__height + self.__width) * 2

    def get_area(self):
        return self.__height * self.__width

    def is_equal(self, p2):
        return self.__a == p2.__a and self.__b == p2.__b and self.__c == p2.__c and self.__d == p2.__d


if __name__ == '__main__':
    p1 = Rectangle(5, 5, 5, 5, 5, 5, 5, 5)
    p2 = Rectangle(10, 5, 10, 5, 10, 5, 10, 5)
    print("perimetr №1:", p1.get_perimeter())
    print("area №1:", p1.get_area())
    print("perimetr №2:", p2.get_perimeter())
    print("area №2:", p2.get_area())
    print("p1 is equal p2 ", p1.is_equal(p2))
