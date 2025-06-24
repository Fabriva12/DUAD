def main():
    result=0
    try:
        my_number= int(input("Ingrese un numero"))
        result+= my_number
        
    except ValueError as error:
        print ("No ingresaste un numero")
        main()
    while True:
        print("Para sumar seleccione s")
        print("Para restar seleccione r")
        print("Para multiplicar seleccione m")
        print("Para dividir seleccione d")
        print("Para borrar resultado seleccione b")
        print("Para salir seleccione z")
        operation = input("")
        if operation == "s": 
                result= addition(result) 
        elif operation == "r": 
                result= subtract(result) 
        elif operation == "m": 
                result= multiplication(result)
        elif operation == "d": 
                result = division(result) 
        elif operation == "b":       
            print(f"El resultado final fue {result}") 
            main()      
        elif operation == "z":       
            print(f"El resultado final fue {result}")
            break


def division(result):
        try:
            number_div= int(input("Ingrese numero que desea dividir"))
            result= result / number_div
            print(f"{result}")
            return result
        except ValueError as error:
            print ("No ingresó un número")
            division(result)

def multiplication(result):
    try:
        number_mult= int(input("Ingrese numero que desea multiplicar"))
        result= result * number_mult
        print(f"{result}")
        return result
    except ValueError as error:
        print ("No ingresó un número")
        multiplication(result)


def subtract(result):
    try:
        number_sub= int(input("Ingrese numero que desea restar"))
        result= result- number_sub
        print(f"{result}")
        return result
    except ValueError as error:
        print ("No ingresó un número")
        subtract(result)


def addition(result):
    try:
        number_add= int(input("Ingrese numero que desea sumar"))
        result= number_add+ result
        print(f"{result}")
        return result
    except ValueError as error:
        print ("No ingresó un número")
        addition(result)

main()