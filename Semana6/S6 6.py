def order_string():
    my_string= input("Ingrese varias palabras separadas por guiones")
    new_string_list = sorted(my_string.split("-"))
    new_string="-".join(new_string_list)
    print(f"{new_string}")

order_string()