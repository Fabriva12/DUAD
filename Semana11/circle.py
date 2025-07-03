class Circle:
    def __init__(self, radius):
        self.radius = radius 
    def get_area(self):
        area = 3.14 * self.radius ** 2
        print (f"{area}")
my_circle = Circle(6)
my_circle_2 = Circle(4)
my_circle.get_area()
my_circle_2.get_area()