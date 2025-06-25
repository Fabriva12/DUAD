def new_student():
    total_student = []
    while True:
        student= input("Quieres agregar un nuevo estudiante (si) (no)")
        if student == "si":
            student_name = input("Cual es el nombre del estudiante")
            student_section = input ("Cual es la seccion del estudiante")
            while True:
                try: 
                    spanish_note = int(input("Cual es la nota de español"))
                    if 0 <= spanish_note <=100:
                        break
                    else :
                        print("No ingresaste una nota entre 0 y 100")
                except ValueError:
                    print("no ingreso una nota valida")
            
            while True:
                try: 
                    english_note = int(input("Cual es la nota de inglés"))
                    if 0 <= english_note <=100:
                        break
                    else :
                        print("No ingresaste una nota entre 0 y 100")
                except ValueError:
                    print("no ingreso una nota valida")
            while True:
                try: 
                    social_est_note = int(input("Cual es la nota de sociales"))
                    if 0 <= social_est_note <=100:
                        break
                    else :
                        print("No ingresaste una nota entre 0 y 100")
                except ValueError:
                    print("no ingreso una nota valida")
            while True:
                try: 
                    science_note = int(input("Cual es la nota de ciencias"))
                    if 0 <= science_note <=100:
                        break
                    else :
                        print("No ingresaste una nota entre 0 y 100")
                except ValueError:
                    print("no ingreso una nota valida")
            average_note = (spanish_note + english_note + social_est_note + science_note)/4
            student_dictionary = [
                {
                "Nombre": student_name,
                "Sección": student_section,
                "Nota de Español": spanish_note,
                "Nota de Inglés": english_note,
                "Nota de Sociales": social_est_note,
                "Nota de Ciencias": science_note,
                "Promedio": average_note
                }
            ]
            total_student.append(student_dictionary)
        elif student == "no":
            break
    
    print (f"{total_student}")

new_student()