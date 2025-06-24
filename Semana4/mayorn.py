major=-9999
counter=0
while counter<10:
    new_number=int(input("Ingrese un numero"))
    counter+=1
    if new_number>major:
        major=new_number
print(f"El mayor numero ingresado fue{major}")