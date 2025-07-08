def print_parameters(func):
    def wrapper (*args):
        print ("Parameter", args)
        result = func(*args)
        print (f"The triangle area is {result}")
    return wrapper

@print_parameters
def get_triangle_area(base, height):
    triangle_area = (base * height) / 2
    return triangle_area

get_triangle_area(4,6)
