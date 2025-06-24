counter= 5

def print_your_self():
    global counter
    name= input ("Ingrese su nombre")
    age= int(input("Ingrese su edad"))
    counter += 1
    print(f"su nombre es {name} y tiene {age} años")
    print (f"{counter}")


print_your_self()


print ("{name}")