time_in_seconds=int(input("Cual es el tiempo en segundos"))
if time_in_seconds<600:
    seconds_missing= 600 - time_in_seconds
    print (f"Los segundos faltantes son {seconds_missing}")
elif time_in_seconds == 600 :
    print("El tiempo es igual a 10 minutos")
elif time_in_seconds > 600:
    print("El tiempo es mayor a 10 minutos")