def is_number_or_not(func):
    def wrapper(*args):
        try: 
            for arg in args:
                if not isinstance(arg, (int, float)):
                    raise ValueError(f"El parámetro '{arg}' no es un número")
            print("Los parámetros son correctos (números).")
            return func(*args)
        except ValueError as e:
            print(e)
    return wrapper


@is_number_or_not
def get_triangle_area(base, height):
    triangle_area = (base * height) / 2
    print(f"The triangle area is {triangle_area}")

get_triangle_area(3, "t6")