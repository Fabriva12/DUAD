def counting_letters():
    my_string = input("Ingrese una oración")
    upper_letter = sum(1 for l in my_string if l.isupper())
    lower_letter = sum(1 for l in my_string if l.islower())
    print(f"Hay {upper_letter} mayusculas y {lower_letter} minusculas")

counting_letters()