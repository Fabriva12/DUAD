while True:
    evalue_number=int(input("Ingrese un numero"))
    if evalue_number %3 ==0 and evalue_number %5 ==0:
        print ("FizzBuzz")
        break
    elif evalue_number %5 ==0:
        print ("Buzz")
        break
    elif evalue_number %3 ==0:
        print ("Fizz")
        break
    else:
        print("El número no es divisible entre 3 o 5")
