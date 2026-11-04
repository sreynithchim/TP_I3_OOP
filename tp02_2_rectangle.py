
class rectangle:
    """A rectangle defined by its width and height."""
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)
    def result(self):
        print("Length of rectangle:", self.length)
        print("Width of rectangle:", self.width)
        print("Area of rectangle:", self.area())
        print("Perimeter of rectangle:", self.perimeter())
        

try:
    length=float(input("Enter the length of the rectangle: "))
    width=float(input("Enter the width of the rectangle: "))
    rect = rectangle(length, width)
    rect.result()
except ValueError as e:
        print("Error : ", e)

