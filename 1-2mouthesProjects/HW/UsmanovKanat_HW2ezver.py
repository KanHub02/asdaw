class Figure:
    unit = "cm"

    def __init__(self):
        pass

    def calculate_area(self):
        pass

    def info(self):
        pass


class Circle(Figure):
    pi = 3.14

    def __init__(self, radius):
        Figure.__init__(self)
        self.__radius = radius

    def calculate_area(self):
        return Circle.pi * self.__radius ** 2

    def info(self):
        return f' Circle radius: {self.__radius}{self.unit},' \
               f'area: {self.calculate_area()}{self.unit}'


class RightTriangle(Figure):
    def __init__(self, side_a, side_b):
        Figure.__init__(self)
        self.__side_a = side_a
        self.__side_b = side_b

    def calculate_area(self):
        return 1 / 2 * (self.__side_a * self.__side_b)

    def info(self):
        return f' RightTriangle side a: {self.__side_a}{self.unit},' \
               f'side b: {self.__side_b}{self.unit},' \
               f'area: {self.calculate_area()}{self.unit}'


Circle_1 = Circle(4)
Circle_2 = Circle(7)
RightTriangle_1 = RightTriangle(4, 6)
RightTriangle_2 = RightTriangle(3, 5)
RightTriangle_3 = RightTriangle(2, 5)

figure = [Circle_1, Circle_2, RightTriangle_1, RightTriangle_2, RightTriangle_3]

for i in figure:
    print(i.info())
