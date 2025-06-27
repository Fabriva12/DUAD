
def menu_action():
    from actions import new_student, show_new_student, average_3, total_average
    from data import export_csv, import_csv
    total_student =[]
    while True:
        chose_main_action = input ("Ingrese (1) para ingresar información  de estudiantes\n"
        "Ingrese (2) para ver la información de todos los estudiantes ingresados\n"
        "Ingrese (3) para ver el top 3 de los estudiantes con la mejor nota promedio\n"
        "Ingrese (4) para ver la nota promedio entre las notas de todos los estudiantes\n"
        "Ingrese (5) para exportar todos los datos actuales a un archivo CSV\n"
        "Ingrese (6) para importar los datos de un archivo CSV previamente exportado\n"
        "Ingrese (7) para salir\n")
        if chose_main_action == "1":
            number_one = new_student()
            total_student.extend(number_one)
        if chose_main_action == "2":
            show_new_student(total_student)
        if chose_main_action == "3":
            average_3(total_student)
        if chose_main_action == "4":
            total_average(total_student)
        if chose_main_action == "5":
            export_csv(total_student)
        if chose_main_action == "6":
            six = import_csv()
        if chose_main_action == "7":
            print("Saliendo del programa, Hasta luego")
            break

