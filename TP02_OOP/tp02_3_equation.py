class EquationCalculator:
    def __init__(self, y, z):
        self.y = y
        self.z = z

    def calculate_x(self):
        if self.y == 0:
            return ValueError("y must not be 0.")
        if self.z == 0:
            return ValueError("z must not be 0.")
        if self.y + self.z == 0:
            return ValueError("y + z must not be 0.")
        return (self.y * self.z) / (self.y + self.z)

    def display_result(self):
            x = self.calculate_x()
            print(f"x = {x}")


try:
    y = float(input("Enter y: "))
    z = float(input("Enter z: "))
    calculator = EquationCalculator(y, z)
    calculator.display_result()
except ValueError:
    print("Error: please enter valid numbers.")