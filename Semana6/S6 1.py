def print_your_self():
    name= input ("Ingrese su nombre")
    age= int(input("Ingrese su edad"))
    
    print(f"su nombre es {name} y tiene {age} años")
    return age


def identify_age(age):
    
    if age<2:
        print ("eres un bebe")
    elif age<12:
        print("eres un niño")
    elif age<18:
        print("eres un adolescente")
    elif age<30:
        print("eres un adulto joven")
    elif age<65:
        print("eres un adulto")    
    elif age>65:
        print("eres un adulto mayor")      


age = print_your_self()
identify_age(age)