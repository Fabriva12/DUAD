fist_name=input("cual es su nombre")
last_name=input("cual es su apellido")
age= int(input("cual es su edad"))
if age<2:
    print(f"{fist_name} {last_name} eres un bebe")
elif age<12:
    print(f"{fist_name} {last_name} eres un niño")
elif age<18:
    print(f"{fist_name} {last_name} eres un adolecente")
elif age<30:
    print(f"{fist_name} {last_name} eres un adulto joven")
elif age<65:
    print(f"{fist_name} {last_name} eres un adulto")
elif age>65:
    print(f"{fist_name} {last_name} eres un adulto mayor")