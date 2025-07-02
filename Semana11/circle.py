class Circle:
    radius = 4
    def get_area(self):
        area = 3.14 * self.radius ** 2
        print (f"{area}")
my_circle = Circle()
my_circle.radius = 6
my_circle_2 = Circle()
my_circle.get_area()
my_circle_2.get_area()