from abc import ABC , abstractmethod

class Shape(ABC):
    
    @abstractmethod
    def area_calculate(self):
        pass
    
    @abstractmethod
    def perimeter_calculate(self):
        pass


class Rectangle(Shape):
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area_calculate(self):
        return self.width * self.height
    
    def perimeter_calculate(self):
        return 2 * (self.width + self.height)


class Circle(Shape):
    
    def __init__(self, radius):
        self.radius = radius
    
    def area_calculate(self):
        return 3.14159 * self.radius * self.radius
    
    def perimeter_calculate(self):
        return 2 * 3.14159 * self.radius


print("Rectangle")
while True:
    width = float(input("Please enter width : "))
    if width > 0:
        break
    print("Please enter number bigger than 0")

while True:
    height = float(input("Please enter height : "))
    if height >= 0:
        break
    print("Please enter number bigger than 0")

rectangle_01 = Rectangle(width, height)

print("\nCircle")
while True:
    radius = float(input("Please enter radius : "))
    if radius >= 0:
        break
    print("Please enter number bigger than 0")

circle_01 = Circle(radius)

shapes_list = [rectangle_01, circle_01]

print("\nResults :")
for i in range(len(shapes_list)):
    shape = shapes_list[i]
    area = shape.area_calculate()
    perimeter = shape.perimeter_calculate()
    
    if i == 0:
        print(f"Rectangle [ Area: {area:.2f}, Perimeter: {perimeter:.2f} ]")
    else:
        print(f"Circle [ Area: {area:.2f}, Perimeter: {perimeter:.2f} ]")