from abc import ABC, abstractmethod

class Shape(ABC):
    
    @abstractmethod
    def calculate_area(self):
        pass
    
    @abstractmethod
    def calculate_perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def calculate_area(self):
        return self.width * self.height
    
    def calculate_perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def calculate_area(self):
        return 3.14159 * self.radius ** 2
    
    def calculate_perimeter(self):
        return 2 * 3.14159 * self.radius

if __name__ == "__main__":

    print("\nMostatil: ")
    while True:
        try:
            width = float(input("width of Mostatil : "))
            height = float(input("height of Mostatil : "))
            if width <= 0 or height <= 0:
                print("Adad bayad bozorgtar az [0] bashand!")
                continue
            break
        except ValueError:
            print("Lotfan faghat [adad] vared konid!")

    print("\nDayere:")
    while True:
        try:
            radius = float(input("radius of Dayere : "))
            if radius <= 0:
                print("radius bayad bozorgtar az [0] bashad!")
                continue
            break
        except ValueError:
            print("Lotfan faghat [adad] vared konid!")

    shapes = [
        Rectangle(width=width, height=height),
        Circle(radius=radius)
    ]

    print("\n" + "=" * 50)
    print("Natayej Mohasebat: ")
    
    for i, shape in enumerate(shapes, 1):
        shape_name = "Mostatil" if i == 1 else "Dayere"
        print("\n" + "-" * 30)
        print(f"{shape_name}:")
        print(f"  Masahat: {shape.calculate_area():.2f}")
        print(f"  Mohit: {shape.calculate_perimeter():.2f}")
    
    print("\n" + "=" * 50)
    print(".....")