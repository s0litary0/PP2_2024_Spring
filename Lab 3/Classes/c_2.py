class Shape:
    def area(self, area = 0):
        print(f"The area of the shape: {area}")

class Square(Shape):
    def __init__(self, length):
        self.length = length
        super().__init__()
        self.square_area = self.length  ** 2

p = Square(int(input("Square length: ")))

p.area(p.square_area)


 
    

