#Inhertiance Code Of Quadrilateral
class Quadrilateral:
    def __init__(self,s1,s2,s3,s4):
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
        self.s4 = s4

    def perimeter(self):
        return self.s1 + self.s2 + self.s3 + self.s4

class Rectangle(Quadrilateral):
    def __init__(self,length,breadth):
        super().__init__(length,breadth,length,breadth)

    def area(self):
        return self.s1 * self.s2

class Square(Quadrilateral):
    def __init__(self,side):
        super().__init__(side,side,side,side)

    def area(self):
        return self.s1 * self.s1

rect = Rectangle(10,5)
print("Perimeter of rectangle is: ",rect.perimeter())
print("Area of rectangle is: ",rect.area())

sq = Square(5)
print("Perimeter of square is: ",sq.perimeter())
print("Area of square is: ",sq.area())
