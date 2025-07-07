from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def  calculate_perimeter(self):
        pass
    @abstractmethod
    def  calculate_area(self):
        pass

class Square(Shape):
    def __init__(self,side):
        self.side = side
    
    def  calculate_perimeter(self,):
        square_perimeter= self.side * 4
        print(f"The square perimeter is {square_perimeter}") 
    
    def  calculate_area(self,):
        square_area = self.side * self.side
        print(f"The square area is{square_area}")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def  calculate_perimeter(self,):
        circle_perimeter = self.radius * 2 * 3.14
        print(f"The circle perimeter is {circle_perimeter}") 
    
    def  calculate_area(self,):
        circle_area = (self.radius **2) * 3.14
        print(f"The circle area is {circle_area}")

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
        
    def  calculate_perimeter(self,):
        triangle_perimeter = self.base + self.base + self.base
        print(f"The triangle perimeter is {triangle_perimeter}") 
    
    def  calculate_area(self,):
        triangle_area = (self.base * self.height )/2
        print(f"The triangle area is {triangle_area}")

square= Square(5)
square.calculate_perimeter()

triangle = Triangle(5,6)
triangle.calculate_area()