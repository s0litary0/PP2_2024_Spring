from c_2 import Shape

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def rect_area(self):
        self.rectangle_area = self.length * self.width

p = Rectangle(int(input("Rectangle length: ")), int(input("Rectangle width: ")))

p.rect_area()

p.area(p.rectangle_area)


