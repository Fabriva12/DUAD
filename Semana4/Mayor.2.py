first_number= int(input("Ingrese primer numero"))
second_number= int(input("Ingrese segundo numero"))
third_number= int(input("Ingrese tercer numero"))
fourth_number= int(input("Ingrese cuarto numero"))
fifth_number= int(input("Ingrese quinto numero"))
major= first_number
if second_number>major:
    major=second_number
if third_number>major:
    major=third_number
if fourth_number>major:
    major=fourth_number
if fifth_number>major:
    major=fifth_number
print (f"el numero mayor es {major}")
