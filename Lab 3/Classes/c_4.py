class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def show(self):
        print(f"({self.x}, {self.y})")

    def move(self, x, y):
        self.x = x
        self.y = y

    def dist(self, x, y):
        print(f"({abs(self.x - x)}, {abs(self.y - y)})")
p = Point(1, 2)
p.show()
p.move(2, 3)
p.show()
p.dist(5, 1)
